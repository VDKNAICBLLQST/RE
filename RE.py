class RE:
    def __init__(self):
        #variables
        self.ETW = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''
        self.rotInfo = {'I':['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''AR<?"=5H_xgC*L78VtQKk|^n h@}{F~#J]Mmv,2!O'$NYp-fGi:4DEd.XcasSoz/0P31TjB+6ueW>qr(U9%\y&Zb;)[wlI''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"II":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''"~dGh|,6_b^4jX5sC&{UN'Ak(/8QT9zV;7!BOo#0]KZLr)J$cyg:fEHD1vF[ a2+I.*<>\ePtqWxlpSm?RnMu@w}=Y-%3i''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"III":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''L)0ud<OsW3&YGT^J;+81M[9Cexl?*EbUygv-n!kH _wm@(V"XFZtq:AchP7/S#B~I4ia,D\=56.po$Q']{>|fRr2z}Nj%K''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"IV":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''{#<^h4iowFa@KIyOW"71?vE~Ggj\.]:MBXfnu|kb,J%!>023dY&L;C+6Qex=ZR_T-Ut'Vp}9mzcSr*($sNH8/l[ qAPD)5''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"V":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''4B0-#%MNkVp89Kj!U{[Z;?E )>]&7um\WIq}Tvyd+3(.DO=CXFb|'oh6Q/5xJSiPa@rfg*,Az^1<l:sG2L$wRc_Yt"ne~H''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"VI":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''sHk]ja^GoP\EcN?Ry 3V:v"~{Ahq6fm&*)+K'w(gx.[05XJ8}D9pO|e>dI1_2/Mn7CWBZ#F;U$@!iz,l-%<=bLYrt4uQTS''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"VII":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''?c|d}4v*Ya-s#9"r5<XoNgx8Vtki[^L,K'j07bU~Tw>PhS q/$FE.1&fI:)2MW\\uZl!OeGQ3(BH%@n={zymD]J6_C;R+pA''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"VIII":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''do4<m[P_cH'$IOi!3Dx%awJsguF]@G*?/0S>K}~rCz\ZjU16by{vkAlhNYVp9L-QB;7 qn)8^fX&tE+M:|"(.T,e2R#=5W''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"IX":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''-03k{&=K?!uaZAhl8C[7y1z6m2c9fPw)M]Rd*4D"n;%i<INVFW>/jE:^($UL~5qXtSYexTvoG _@QJ#p,|HB'sOg.r\\b+}''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"X":['''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>''','''2d#kw)(!D/B%r,Sm8qsA{}F0\'cX:9aNx[*\\ JRhgjvQ$iUyTf<+&P>4t]G|Zo3eVH"-^7MW~LpKI@zb65.unCY;l_=E1O?''','''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$_&-+()/*"':;!?,.~=\\^|%[]{} <>'''],"A":'''(1UR6cGTNLKJ7I?P:DaHCV~n;*SqFd4{grsok0)Xjpbhitu>wx5@lB2_eyEM"\z!+3&[$Am^Z8'QY#O.,W=9/|]-%f} <v''',"B":'''aONDG@EWvRKL%CBs;J0~U:H,5ZAwg|"fckp<hl>?oi9_PtzIbyxuS1('+Y76[qF! r&-42./*e3VQ#nX)T=\^dM8]{}$jm''',"C":'''iZI@]{PLC?hHzYOGXVST#R~QNBev57a-wKAjrl:,'p_ks[$bg9%M0/2;4c!d8xDUuq f+()1*"om36Jn^W=|.\ytEF}&<>''',"D":'''m\\2DEd(/I%;oar$Wcz.jU@PkZYMbQFx:n+{TX~AgL1qN?| &4e]R)pC3w56[8-V>O_v9hG0H*"'fK!s,Sl=B^tJ7yi}u<#'''}
        self.notchInfo = {'I':'a',"II":'R',"III":'0',"IV":'2',"V":'d',"VI":'@',"VII":'&',"VIII":'W',"IX":'|',"X":'~'}
        self.plugBoardDict = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '@': '@', '#': '#', '$': '$', '_': '_', '&': '&', '-': '-', '+': '+', '(': '(', ')': ')', '/': '/', '*': '*', '"': '"', "'": "'", ':': ':', ';': ';', '!': '!', '?': '?', ',': ',', '.': '.', '~': '~', '=': '=', '\\': '\\', '^': '^', '|': '|', '%': '%', '[': '[', ']': ']', '{': '{', '}': '}', ' ': ' ', '<': '<', '>': '>'}
        self.plugBoard,self.reflector = "",""
        self.rotors,self.rings,self.initalPos,self.rotorsInitialInfo = [],[],[],[]
    
    def Settings(self,rotI="I",rotII="II",rotIII="III",rotIV="IV",rotV="V",rinI="A",rinII="A",rinIII="A",rinIV="A",rinV="A",iniPosI="A",iniPosII="A",iniPosIII="A",iniPosIV="A",iniPosV="A",refl="A",plugboard=""):
       
        #set the given initial_settings
        self.rotorsInitialInfo = [self.rotInfo[rotI],self.rotInfo[rotII],self.rotInfo[rotIII],self.rotInfo[rotIV],self.rotInfo[rotV]]
        self.rotors = [self.rotInfo[rotI],self.rotInfo[rotII],self.rotInfo[rotIII],self.rotInfo[rotIV],self.rotInfo[rotV],self.rotInfo[refl]]
        self.rings = [rinI,rinII,rinIII,rinIV,rinV]
        self.initalPos = [iniPosI,iniPosII,iniPosIII,iniPosIV,iniPosV]
        self.plugBoard = plugboard
        self.reflector = refl

        #check_plugboard
        self.plugBoard = self.plugBoard.split("-S-")
        temp = ''.join(self.plugBoard)
        for i in temp:
            if temp.count(i) > 1:
                raise AttributeError
        
        #set_plugBoardDict
        for i in self.plugBoard:
            if len(i) == 2:
                self.plugBoardDict[i[0]] = i[1]
                self.plugBoardDict[i[1]] = i[0]
            elif len(i) == 1 or len(i) > 2:
                raise AttributeError
                
        
        #set rotor's & ring's initial positions
        for i in range(0,5):
            self.rotors[i][2] = self.rotors[i][2][self.rotors[i][2].index(self.rings[i]):] + self.rotors[i][2][:self.rotors[i][2].index(self.rings[i])]
            self.rotors[i][0] = self.rotors[i][0][self.rotors[i][2].index(self.initalPos[i]):] + self.rotors[i][0][:self.rotors[i][2].index(self.initalPos[i])]
            self.rotors[i][1] = self.rotors[i][1][self.rotors[i][2].index(self.initalPos[i]):] + self.rotors[i][1][:self.rotors[i][2].index(self.initalPos[i])]
            self.rotors[i][2] = self.rotors[i][2][self.rotors[i][2].index(self.initalPos[i]):] + self.rotors[i][2][:self.rotors[i][2].index(self.initalPos[i])]
    
    #get_keys from values
    def getKeys(self,dic,val):
        for key,value in dic.items():
            if val==value:
                return key
    
    #getDetails
    def getDetails(self):
        details = (self.getKeys(self.rotInfo,self.rotorsInitialInfo[0]),self.getKeys(self.rotInfo,self.rotorsInitialInfo[1]),self.getKeys(self.rotInfo,self.rotorsInitialInfo[2]),self.getKeys(self.rotInfo,self.rotorsInitialInfo[3]),self.getKeys(self.rotInfo,self.rotorsInitialInfo[4]),self.rings[0],self.rings[1],self.rings[2],self.rings[3],self.rings[4],self.initalPos[0],self.initalPos[1],self.initalPos[2],self.initalPos[3],self.initalPos[4],self.plugBoard,self.reflector)
        return details

re = RE()
re.Settings()
print(re.getDetails())