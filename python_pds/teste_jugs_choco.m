% Leitura e filtragem do sinal:
[s,fa] = audioread('choco.wav');
ss = s;
s = s(2:end) - 0.95*s(1:end-1); %passa altas


% Análise:
Janela = round(0.03*fa);
Avanco = round(0.01*fa);
Ordem = round(0.001*fa);
CP = [];
Pot = [];
TCZ = [];
for k = 1:Avanco:(length(s)-Janela) 
    saux = s(k:k+Janela-1); 
    Pot = [Pot mean(saux.^2)];  
    pz = find(saux(2:end)>0 & saux(1:end-1)<0); 
    TCZ = [TCZ length(pz)*fa/Janela];
    S = [];
    for m = 1:Ordem+1
        S = [S saux(m:end-(Ordem+1)+m)];
    end
    C = pinv(S(:,1:end-1))*S(:,end); 
    CP = [CP C];
end


% Ressíntese
K = length(s);
perfilTempo = 0.1 + 4*([0:K]/K);
apontador = floor(cumsum(perfilTempo));
N = apontador(end);
perfilF0 = 80-30*([0:N]/N);
r = randn(1,N);
v = zeros(1,N);
pp = round(fa/perfilF0(1));
v(pp) = 1;

while pp<N
    pp = pp + round(fa/perfilF0(pp));
    v(pp) = 1;
end
N1 = fa*0.001;
N2 = fa*0.0005;
g = [0.5*(1-cos(pi*[0:N1]/N1)) sin(pi*[0:N2]/(2*N2))];
v = conv(g,v);
v = v/std(v);
y = zeros(1,N);
[ordem,ncol] = size(CP);
passo = floor(K/ncol);
n_ini = ordem+1;
for col = 1:ncol
    if TCZ(col)<2000
        vozeado = 0.9;
    else
        vozeado = 0.1;
    end
    ganho = sqrt(Pot(col));
    n_fim = apontador(passo*col);
    for n = n_ini:n_fim
        y(n) = y(n-1:-1:n-ordem)*CP(end:-1:1,col) + ganho*(vozeado*v(n)+(1-vozeado)*r(n));
    end
    n_ini = n_fim;
end
y = y/max(abs(y));
soundsc(ss,fa);
pause(100e-2);
soundsc(s,fa);
pause(100e-2)
soundsc(y,fa);