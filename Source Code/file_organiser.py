import os
from shutil import move,copy
import time
from time import sleep
import datetime

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for file in filenames:
            yield os.path.abspath(os.path.join(dirpath, file))

def target_dirs():
    thisFile=os.path.dirname(__file__)
    path=os.path.join(os.path.abspath(thisFile),'ORGANISED FILES')
    try:
        os.mkdir(path)
    except:
        print('Main folder not created')
    dirs={
        'images':os.path.join(os.path.abspath(path),'Image files'),
        'videos':os.path.join(os.path.abspath(path),'Video files'),
        'audios' :os.path.join(os.path.abspath(path),'Audio files'),
        'documents':os.path.join(os.path.abspath(path),'Documents'),
        'zip':os.path.join(os.path.abspath(path),'Zip files'),
        'other':os.path.join(os.path.abspath(path),'Other files'),
        'backup':os.path.join(os.path.abspath(thisFile),'Backup'),
        'log':os.path.join(os.path.abspath(path),'LOG REPORT')
    }
    return dirs

def root_dirs():
    thisFile=os.path.dirname(__file__)
    path=os.path.join(os.path.abspath(thisFile),'editable_files','directories.txt')
    with open(path,"r") as f:
        dirList=f.read().splitlines()
    files=[]
    for path in dirList:
        x=absoluteFilePaths(path)
        for y in x:
            files.append(y)
    return files

target_directories=target_dirs()
file_dirs=[]


for file in root_dirs():
    file_dirs.append(file)

if len(file_dirs)==0:
    print('The directory/s you entered are empty')
    os.system('pause')
    exit()



pdf_documents=[]
word_documents=[]
spread_documents=[]
presentation_documents=[]
zip_files=[]
pictures=[]
videos=[]
audios=[]
other_files=[]

log=[]

total_files=0
completed=0
skippd_files=0

for file in file_dirs:
    try:
        if file.split('.')[1].lower() == 'pdf':
            pdf_documents.append(file)
        elif file.split('.')[1].lower() in ['doc','docx']:
            word_documents.append(file)
        elif file.split('.')[1].lower() in ['zip','rar']:
            zip_files.append(file)
        elif file.split('.')[1].lower() in ['jpg','jpeg','gif','tiff','png','bmp','webp']:
            pictures.append(file)
        elif file.split('.')[1].lower() in ['mp4','mov','wmv','flv','avi','mkv','webm']:
            videos.append(file)
        elif file.split('.')[1].lower() in ['xls','xlsm','xlsx','csv','ots']:
            spread_documents.append(file)
        elif file.split('.')[1].lower() in ['pptx','pptm','ppt']:
            presentation_documents.append(file)
        elif file.split('.')[1].lower() in ['wav','mp3','ppt','aiff','flac','bwf','aac']:
            audios.append(file)
        else:
            other_files.append(file)
        total_files+=1
    except:
        log.append(f"None type file found")
        skippd_files+=1


try:
    os.mkdir(target_directories['backup'])
except:
    log.append("Backup folder already exist")


print('\r')

if len(pdf_documents)>0:

    try:
        os.mkdir(target_directories['documents'])
    except:
        pass

    pdf_path = os.path.join(target_directories['documents'],'PDF Files')

    try:
        os.mkdir(pdf_path)
    except:
        pass

    for direc in pdf_documents:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")

        finalPath=os.path.join(pdf_path,time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")
        completed+=1
        
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')


        
if len(word_documents)>0:
    sleep(1)

    try:
        os.mkdir(target_directories['documents'])
    except:
        pass

    word_path = os.path.join(target_directories['documents'],'Word Documents')

    try:
        os.mkdir(word_path)
    except:
        pass

    for direc in word_documents:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")

        finalPath=os.path.join(word_path,time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")

        completed+=1
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')

if len(spread_documents)>0:
    sleep(1)

    try:
        os.mkdir(target_directories['documents'])
    except:
        pass

    spread_path=os.path.join(target_directories['documents'],'Spread Sheets')

    try:
        os.mkdir(spread_path)
    except:
        pass

    for direc in spread_documents:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")

        finalPath=os.path.join(spread_path,time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")
        completed+=1
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')

if len(presentation_documents)>0:
    
    sleep(1)

    try:
        os.mkdir(target_directories['documents'])
    except:
        pass

    presentation_path=os.path.join(target_directories['documents'],'Presentation files')

    try:
        os.mkdir(presentation_path)
    except:
        pass

    for direc in presentation_documents:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")

        finalPath=os.path.join(presentation_path,time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")
        completed+=1
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')

if len(pictures)>0:
    sleep(1)
    try:
        os.mkdir(target_directories['images'])
    except:
        pass

    for direc in pictures:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")
        
        finalPath=os.path.join(target_directories['images'],time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")
        completed+=1
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')

if len(videos)>0:
    sleep(1)

    try:
        os.mkdir(target_directories['videos'])
    except:
        pass

    for direc in videos:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")

        finalPath=os.path.join(target_directories['videos'],time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")
        completed+=1
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')

if len(audios)>0:
    sleep(1)

    try:
        os.mkdir(target_directories['audios'])
    except:
        pass

    for direc in audios:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")

        finalPath=os.path.join(target_directories['audios'],time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")
        completed+=1
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')

if len(other_files)>0:

    sleep(1)
    
    try:
        os.mkdir(target_directories['other'])
    except:
        pass

    for direc in other_files:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")

        finalPath=os.path.join(target_directories['other'],time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")
        completed+=1
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')

if len(zip_files)>0:
    sleep(1)
    
    try:
        os.mkdir(target_directories['other'])
    except:
        pass
    
    for direc in zip_files:

        try:
            copy(direc,target_directories['backup'])
        except:
            log.append(f"File:[{direc}] didn't copied to the backup.")

        finalPath=os.path.join(target_directories['zip'],time.strftime("%Y-%m",time.strptime(time.ctime(os.path.getmtime(direc)))))
        try:
            os.mkdir(finalPath)
        except:
            pass

        try:
            move(direc,finalPath)
        except:
            log.append(f"File: {direc} failed. File may already in destination")
        completed+=1
        print("Processing {}%".format(round((completed/total_files)*100,2)),end='\r')

print(f"\r Processing {(completed/total_files)*100} % ")

try:
    os.mkdir(target_directories['log'])
except:
    log.append("Log folder already exist")

with open(os.path.join(target_directories['log'],'log_report.txt'),"w") as f:
    f.write(f'Date and time: {datetime.datetime.now()} \n\n')
    for i in log:
        f.write(i+"\n")
    f.write(f'\n\nNumber of skipped files:{skippd_files}')
    f.write('\n')
    f.write('----------------------------------------------------------------\n\n')

os.system("pause")