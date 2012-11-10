// Em ChucK, soltar estas duas linhas em alguma música
// bem ritmada e deixar os padrões à vontade com este
// arco maior:

// stupidly rising
SinOsc s1 => Gain g => g => s1 => dac;
2 => s1.sync;
while(second => now);

// crazy wind through a window
Noise s1 => Gain g1 => g1 => SinOsc s2 => dac;
2 => s2.sync;
while(second => now);