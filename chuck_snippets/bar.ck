// Em ChucK, soltar estas duas linhas em alguma musica
// bem ritmada e deixar os padroes aa vontade com este
// arco maior:

// crescimento continuo
SinOsc s1 => Gain g => g => s1 => dac;
2 => s1.sync;
while(second => now);

// vento
Noise s1 => Gain g1 => g1 => SinOsc s2 => dac;
2 => s2.sync;
while(second => now);
