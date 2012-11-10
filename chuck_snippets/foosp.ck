public class Foo {
    static string name[];
    static float prop[];
    static float rate[];
    static float du[];
    static float gain[];
}

["samples/fx/s22.wav"] @=> Foo.name;
[.0] @=> Foo.prop;
[1.] @=> Foo.rate;
[4.] @=> Foo.du;
[0.] @=> Foo.gain;

TimeGrid tg;
tg.set(1::minute/60/2, 8, 10);
tg.sync();

SndBuf buf => JCRev j => dac;
.5 => j.gain;
.2 => j.mix;

0 => int i;

while (true) {
    Foo.name[0] => buf.read;
    Math.trunc(buf.samples()*Foo.prop[i%Foo.prop.size()]) $ int => buf.pos;
    Foo.gain[i%Foo.gain.size()] => j.gain;
    Foo.rate[i%Foo.rate.size()] => buf.rate;
    tg.beat*Foo.du[i%Foo.du.size()] => now;
    i++;
} 