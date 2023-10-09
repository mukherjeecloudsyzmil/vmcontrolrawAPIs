import subprocess

def start_vm(vm_name):
    subprocess.run(["VBoxManage", "startvm", vm_name])

def stop_vm(vm_name):
    subprocess.run(["VBoxManage", "controlvm", vm_name, "poweroff"])

# Example usage:
start_vm("centos7-server")
stop_vm("centos7-server")
