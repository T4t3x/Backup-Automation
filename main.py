import os, shutil, datetime, schedule, time

source = "C:/Users/Usuario/Documents/UNI - ALEX/backup_automation/origin"
destination = "C:/Users/Usuario/Documents/UNI - ALEX/backup_automation/backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Error already exists in: {dest}")

def l():
    copy_folder_to_directory(source,destination)

def main():
    schedule.every().week.at("6:00").do(l)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()