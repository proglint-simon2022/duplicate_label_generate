import os

label_path = r'C:\Users\PLAP013\Downloads\DUPLICATES\0th_label'
duplicate_path = r'C:\Users\PLAP013\Downloads\DUPLICATES\remain_images'

all_label_list = []

for label in os.listdir(label_path):
    all_label_list.append(label)

for session_id in os.listdir(duplicate_path):
    for sub_folder in os.listdir(f'{duplicate_path}\{session_id}'):
        dest_path = f'{duplicate_path}\{session_id}\{sub_folder}'
        for image in os.listdir(dest_path):
            img_name = image[:-4]
            name_list = image.split('_')
            name = ''.join(name_list[:-1])
            for label in all_label_list:
                label_list = label.split('_')
                label_new = ''.join(label_list[:-1])
                if label_new == name:
                    content = open(f'{label_path}\{label}', 'r').read()
                    with open(dest_path + "/" + img_name +".txt", "a") as f:
                        for txt in content:
                            f.write(f'{txt}')
                    f.close()
            print(f'{image} is done.')
print('finished...')                            
                            
