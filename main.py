import os

# go.mod search
def findProjects(base_path):
    projects = []
    for root, dirs, files in os.walk(base_path):
        if "go.mod" in files:
            projects.append(root)
    return projects

# deep search
def deepSearch(base_path):
    projects = []
    for root, dirs, files in os.walk(base_path):
        if "go.mod" in files:
            projects.append(root)
    return projects

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    projects = findProjects(base_path)
    if not projects:
        print("No project with go.mod found in this folder. Searching deeply...")
        projects = deepSearch(base_path)
        if not projects:
            print("Still no project with go.mod found in all subfolders.")
            return

    print("List of Go projects found:")
    for idx, proj in enumerate(projects):
        print(f"{idx+1}. {os.path.relpath(proj, base_path)}")

    try:
        pilihan = int(input("Select the project number to switch to (int): "))
        if pilihan < 1 or pilihan > len(projects):
            print("Invalid selection.")
            return
    except ValueError:
        print("Input must be a number.")
        return

    target_path = projects[pilihan-1]
    go_work_path = os.path.join(base_path, "go.work")
    rel_mod_path = os.path.relpath(target_path, base_path)
    with open(go_work_path, "w") as f:
        f.write("go 1.24\n\n") # change to your current go version
        f.write("use ./"+rel_mod_path.replace("\\", "/")+"\n")
    print(f"go.work has been created and pointed to: {rel_mod_path}")

if __name__ == "__main__":
    main()
