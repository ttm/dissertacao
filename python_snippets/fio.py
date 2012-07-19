import wave, struct
class IOUtils:
    def recordPattern(self,filename,pattern):
    	self.recordFile(pattern.sonic_vector,[],"sound.wav",pattern.SR)
	
    def recordFile(self, sonic_vector=[], sonic_vector2=[],
                         filename="sound.wav", samplerate=44100):
    	sound = wave.open(filename,'w')
    	sound.setframerate(samplerate)

    	sound.setsampwidth(2) # Always 16bit/sample (2 bytes)
    	if not sonic_vector2:
    	    sound.setnchannels(1) # Mono
	        sonic_vector=self.boundVector(sonic_vector)

	        sonic_vector=[i*(2**15-1) for i in sonic_vector]
	        sound.writeframes(struct.pack('h'*len(sonic_vector),
                                    *[int(i) for i in sonic_vector]))
    	else:
	        sound.setnchannels(2) # stereo
    	    sonic_vector=self.boundVector(sonic_vector)
    	    sonic_vector2=self.boundVector(sonic_vector2)

    	    sonic_vector=[i*(2**15-1) for i in sonic_vector]
    	    sonic_vector2=[i*(2**15-1) for i in sonic_vector2]
    	    SV=[]
    	    for i,j in zip(sonic_vector,sonic_vector2):
        		SV.extend((i,j))
	        sound.writeframes(struct.pack('h'*len(SV),*SV))
    	sound.close()

    def boundVector(self,vector):
 	 	"""Bound vector in the [-1,1] interval"""
 		svmin=min(vector)
 		svmax=max(vector)
 		ambit=svmax-svmin
 		if svmax>1 or svmin<-1:
 		    if svmax-svmin > 2:
  				i=0
  				for sample in vector:
  				    new_sample=(sample-svmin)/ambit # results in [0,1]
  				    new_sample=new_sample*2-1 # results in [-1,1]
  				    vector[i]=new_sample
  				    i+=1
 		    elif svmax > 1:
  				offset=svmax-ambit/2
  				i=0
  				for sample in vector:
  				    new_sample=sample - offset
  				    vector[i]=new_sample
  				    i+=1
 		    elif svmin < -1:
  				offset=-svmin -ambit/2
  				i=0
  				for sample in vector:
  				    new_sample=sample + offset
  				    vector[i] = new_sample
  				    i+=1
 		return vector
