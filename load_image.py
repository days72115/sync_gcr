# coding:utf-8
import subprocess, os
def get_filename():
    with open("images.txt", "r") as f:
        lines = f.read().split('\n')
        # print(lines)
        return lines



def pull_image():
    name_list= get_filename()
    for name in name_list:
        if 'sha256' in name:
            print(name)
            sha256_name = name.split("@")
            new_name_t = sha256_name[0].split("/")[-1]
            tag = sha256_name[-1].split(":")[-1][0:6]
            new_name = "kenwood/" + new_name_t + ":"+ tag
        else:
            new_name = "kenwood/" + name.split("/")[-1]
        print(new_name)
        subprocess.call("docker pull {}".format(new_name), shell=True)
        subprocess.run(["docker", "tag", new_name, name])
        subprocess.call("docker rmi  {}".format(new_name), shell= True)
if __name__ == "__main__":
    pull_image()
