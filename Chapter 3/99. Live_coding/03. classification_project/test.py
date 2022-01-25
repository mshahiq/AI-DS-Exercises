# import os

# img_folder = 'img'

# classes = os.listdir(img_folder)

# paths = ['train', 'test']

# # for f in img_folder:
# #     for p in f:
# #         print(p)

# # for item in paths:
# #     for i in range(len(classes)):
# #         os.system(f'mkdir -p ./datasets/{item}/{str(i)}')

# # os.system('mv /path/to/the/source path/to/destination')
# # 'img/person/0_7.png'

# # files = os.listdir(img_folder + '/' + classes[0])

# path_to_img = 'img'+'/'+'person'

# # print(path_to_img)

# files = os.listdir(path_to_img)
# files = sorted(files)
# print(files[1])

# # for item in classes:
# #     for i in range(len(item)):
# #         print(item[i])


#################################################### OOP #########################################################################
import os
class list_folder_path:

    def __init__(self, path) -> None:
        self.path = path

    def image_path(self):
        
        filename = os.listdir(self.path)


        for in_filename in filename:
            path_to_animals = self.path + '/'+ in_filename
            inside_file = os.listdir(path_to_animals)
            path_to_animals = sorted(path_to_animals)
        
            # print(os.path.abspath(os.path.join(self.path,in_filename)), sep='\n')
        
            for animals in inside_file:
                animals_toimage = self.path + '/'+ in_filename + '/' + animals
                anim_images = os.listdir(animals_toimage)
                animals_toimage = sorted(animals_toimage)

                # print(os.path.abspath(os.path.join(self.path,in_filename,animals)), sep='\n')
            
                for individualimage in anim_images:
                    print(os.path.abspath(os.path.join(self.path,in_filename,animals,individualimage)))


det_file_path = list_folder_path('images')
det_file_path.image_path()
