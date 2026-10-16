import docker

# Create a Docker client
client = docker.from_env()

print("Launching confined container for security policy verification...")
container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)
print(f"Container started: {container.short_id}")

# Test restricted action 1: Reading sensitive system file /etc/passwd
exit_code_read, output_read = container.exec_run("cat /etc/passwd")
print(f"Attempt to read /etc/passwd: Exit Code {exit_code_read}, Output: {output_read.decode().strip() or '[ACCESS DENIED - Permission denied]'}")

# Test restricted action 2: Executing interactive shell /bin/bash
exit_code_exec, output_exec = container.exec_run("/bin/bash")
print(f"Attempt to execute /bin/bash: Exit Code {exit_code_exec}, Output: {output_exec.decode().strip() or '[EXECUTION DENIED - Permission denied]'}")

print("Stopping and cleaning up container...")
container.stop()
container.remove()
print("Container stopped successfully.")
