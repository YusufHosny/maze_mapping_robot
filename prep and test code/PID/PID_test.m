tstart = 0;
tend = 5;
tstep = 0.0001;

t = (tstart:tstep:tend)';

R = 1e3;
C = 1e-3;
sys = tf([1], [R*C 1]);

%%
Kc = 1;
Ti = 0.1; 
Tc = tf([Kc*Ti, Kc], [Ti, 0]); 
cloop = feedback(Tc*sys, 1);
step(cloop);

%%
Kc = 0.6;
Ti = 1/10;
Td = 1;
Tc = tf([Kc*Td*Ti, Kc*Ti, Kc], [Ti, 0]);

cloop = feedback(Tc*sys, 1)
pzmap(cloop)
step(cloop);