from pyngrok import ngrok as ng



class NgrokApi:
      def __init__(self , Port,Protocol):
         self.Port = Port
         self.Protocol = Protocol
         self.NgrokUrl= ""
         self.SupportList = ['http', 'tcp']
         self.ProtocolVerify = False
         self.PortVerify = False
      def CheckProtocol(self):
          if self.Protocol in self.SupportList:
             self.ProtocolVerify = True
             return True
          else:
              self.ProtocolVerify = False
              return False
      def CheckPort(self):
          if self.Port > 1024:
             self.PortVerify = True
             return True
          else:
              self.PortVerify = False
              return False
      def Connect(self):
          if self.PortVerify and self.ProtocolVerify:
             self.NgrokUrl = ng.connect(self.Port,self.Protocol)
             return True
          else :
              return True
      def Disconnect(self):
          if self.NgrokUrl != None:
             ng.disconnect(self.NgrokUrl)
             return True
          else:
              return False
