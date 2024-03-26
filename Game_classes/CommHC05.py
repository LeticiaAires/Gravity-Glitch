
import time
import serial

class MyCommHC05:
        def __init__(self):
            self.ser = serial.Serial(port = "COM11", baudrate=115200, parity = serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, bytesize= serial.EIGHTBITS, timeout=0)
            # pour le lissage expo et le filtre passe haut
            self.last_alt = 0
            # pour le filtre passe haut
            self.last_filtered_alt = 0
            


        def get_altitude(self) :
            line = self.ser.readline().rstrip().decode()
            if line:
                alt = int(line)

                # aller sur https://cpge.frama.io/fiches-cpge/Python/Filtres/80%20-%20Filtrage/ pour des idées de lissage/filtrage
                
                #sans filtrage
                #return alt 

                #lissage exponentiel
                return self.lissage_exponentiel(alt)

                #filtre passe haut 1er ordre
                #return self.passe_haut_1er_ordre(alt)

            else :
                return None
        
        def __del__(self):
            self.ser.close()

        def lissage_exponentiel(self,alt):
            # Constantes à étudier...
            N = 10
            alpha = 2/(N+1)

            new_alt = alpha*alt+(1-alpha)*self.last_alt
            self.last_alt = new_alt
            return new_alt

        def passe_haut_1er_ordre(self, alt):
            #Constantes à étudier...
            fc = 100  # Hz
            tau = 1/(2*3.14*fc)
            Te = 2.7e-7 #1 nombre de 4 octects sur 115200 bauds
            
            filtered_alt = self.last_filtered_alt*(1-Te/tau)+alt-self.last_alt
            self.last_filtered_alt = filtered_alt
            self.last_alt = alt

            return filtered_alt


