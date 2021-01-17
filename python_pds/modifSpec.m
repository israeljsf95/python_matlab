function [NCP]=modifSpec(CP, fator, fa)

cosAngMin = cos(100*2*pi/fa); % O menor ângulo a ser modificado corresponde a 100 Hz
cosAngMax = cos(3000*2*pi/fa); % O maior ângulo a ser modificado corresponde a 3000 Hz
[ordem,ncol] = size(CP);
NCP = zeros(ordem,ncol);

for col=1:ncol

    C = CP(:,col);
    H = polyfit([-C; 1]);
    H = fliplr(H);
    R = roots(H);
    ro = abs(R);
    % Alteração de formantes entre 100 Hz e 3000 Hz
    a = real(R);
    b = imag(R);
    deltaW = fator*atan(b./a);
    posPolosSup = find(b>0 & ro>0.9 & a<=cosAngMin & a>=cosAngMax);
    posPolosInf = find(b<0 & ro>0.9 & a<=cosAngMin & a>=cosAngMax);
    NR = R;
    NR(posPolosSup) = (a(posPolosSup).*cos(deltaW(posPolosSup))-b(posPolosSup).*sin(deltaW(posPolosSup)))+ ii*(b(posPolosSup).*cos(deltaW(posPolosSup))+a(posPolosSup).*sin(deltaW(posPolosSup)));
    NR(posPolosInf) = (a(posPolosInf).*cos(deltaW(posPolosSup))+b(posPolosInf).*sin(deltaW(posPolosSup)))+ ii*(b(posPolosInf).*cos(deltaW(posPolosSup))-a(posPolosInf).*sin(deltaW(posPolosSup)));
    aux = real(poly(NR))';
    NCP(:,col) = -aux(1:end-1);

end

end