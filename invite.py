def write_code(invitecode):
    if len(invitecode)==12:
        with open('num.txt','r') as g:
            t=g.read()
        with open("invite.txt","r") as f:
            s=f.readlines()
            invitecodes=invitecode+'\n'
            if len(s)>=int(t) or invitecodes in s:
                return False
            else:
                f=open('invite.txt','a')
                f.write(invitecodes)
                f.close()
                return True
    else:
        return False
def delete_code():
    with open ('invite.txt','w') as f:
        f.write('')
    with open('log2.log','w') as g:
        g.write('') 
    return True
          
def code_num(num):
    if num.isdigit():
        s=open('num.txt','w')
        s.write(num)
        s.close()
        return True 
    else:return False 
def main():
    print('happy new year!') 
    
    
if __name__=="__main__":
    main()
