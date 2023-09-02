
import os
content='''
// Init_PORTA
void Init_PORTA_DIR(void)
{
    DDR=0b010010101;
    feno;
    lolo
}
'''
def create_file_withnew_dir(path_dir,path_file):  
 if not os.path.exists(path_dir):
    os.mkdir(path_dir)
    with open(path_file,"w") as fd:
       fd.write(content)

# that is for write txt file

def create_file_withnew_file(dir_name,path_dir,path_file):  
 for root,dirs,files in os.walk(path_dir):
    if(file_name in files):
        pass
    else:
        with open(path_file,"w") as fd:
         fd.write(content)
           
root=os.getcwd()
path_dir=root+"/Dion_init"
file_name="init.txt"
path_file=path_dir+'/init.txt'  
# the main code
l=[]
for i in range(0,8):
    x=input(f"plz enter bit{i}: ")
    l.append(str(x))

result=''.join(l)
total="0b"+result
create_file_withnew_dir(path_dir,path_file)
with open(path_file,"r") as fd:
    contxt=fd.readlines()
with open(path_file,"w") as fd:
 for index,line in enumerate(contxt):
     if(index==4):
         modified_line=f"   DDR={total} "
         fd.write(modified_line)
     else:
         fd.write(line)  
fd.close()              
with open(path_file,"r") as fd:
    lst=fd.readlines()
    for line in lst:
        print(line)    
