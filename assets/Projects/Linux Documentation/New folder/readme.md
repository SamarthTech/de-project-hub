
# Linux Command Line Documentation


![MySQL Logo](https://images.vexels.com/media/users/3/140692/isolated/lists/72d1f12edf758d24f5b6db73bac4f297-linux-logo.png)



Welcome to the **Linux Command Line Documentation**! This guide covers Linux command basics, advanced tricks, and practical tips to help you unlock the power of the Linux terminal. Whether you're just starting out or are an experienced user, these commands, tips, and examples will help streamline your workflow.

---

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Basic Commands](#basic-commands)
  - [Navigating Directories](#navigating-directories)
  - [File Operations](#file-operations)
- [System Information and Monitoring](#system-information-and-monitoring)
- [Process Management](#process-management)
- [Permissions Management](#permissions-management)
- [Networking Essentials](#networking-essentials)
- [Shell Scripting Basics](#shell-scripting-basics)
- [Pro Tips and Tricks](#pro-tips-and-tricks)
- [Additional Resources](#additional-resources)

---

## Introduction

The **Linux Command Line Interface (CLI)** is a powerful tool that gives users direct control over the operating system. Mastering the CLI enables users to automate tasks, troubleshoot efficiently, and perform complex actions with simple commands.

---

## Getting Started

1. **Opening the Terminal**:
   - Use `Ctrl + Alt + T` on most Linux distributions.
   - Alternatively, press `Ctrl + Alt + F1` to open a TTY session (press `Ctrl + Alt + F7` to return to GUI).

2. **Essential Commands**:
   - **`man`** - Shows the manual for any command.
     ```bash
     man ls  # Opens the manual for 'ls'
     ```

3. **Autocompletion and History**:
   - Use `Tab` to autocomplete commands and filenames.
   - Press the `↑` and `↓` arrows to browse through command history.

---

## Basic Commands

### Navigating Directories

1. **`pwd`** - Prints the current working directory.
   ```bash
   pwd
   ```

2. **`ls`** - Lists files and directories.
   ```bash
   ls          # Basic listing
   ls -l       # Detailed listing with permissions and file sizes
   ls -lh      # Human-readable file sizes
   ls -a       # Show hidden files (files that start with '.')
   ```

3. **`cd`** - Changes the directory.
   ```bash
   cd /path/to/directory  # Go to specific directory
   cd ..                  # Move up one level
   cd ~                   # Move to home directory
   cd -                   # Go back to the last directory
   ```

   **Tip**: Use `cd ~` for a quick return to the home directory, or `cd -` to switch back to the last location you were in.

---

### File Operations

1. **`touch`** - Creates a new empty file.
   ```bash
   touch filename.txt
   ```

2. **`cp`** - Copies files or directories.
   ```bash
   cp file1.txt /destination/directory
   cp -r /source/directory /destination/directory  # Copy directories recursively
   ```

3. **`mv`** - Moves or renames files or directories.
   ```bash
   mv oldname.txt newname.txt       # Rename file
   mv file.txt /destination/directory
   ```

4. **`rm`** - Deletes files or directories.
   ```bash
   rm filename.txt                 # Delete file
   rm -r /path/to/directory        # Delete directory recursively
   rm -i filename.txt              # Interactive mode, confirms before deleting
   ```

5. **File Viewing Commands**:
   - **`cat`** - Displays file contents.
     ```bash
     cat filename.txt
     ```

   - **`less`** - Views file with scrollable interface.
     ```bash
     less filename.txt
     ```

   - **`head`** and **`tail`** - Shows the start or end of a file.
     ```bash
     head -n 10 filename.txt   # View first 10 lines
     tail -n 10 filename.txt   # View last 10 lines
     tail -f log.txt           # Follow live updates (useful for monitoring logs)
     ```

---

## System Information and Monitoring

1. **`uname`** - Displays system information.
   ```bash
   uname -a    # Print all system information
   ```

2. **`df`** - Disk usage of filesystems.
   ```bash
   df -h       # Human-readable format
   ```

3. **`du`** - Disk usage of files and directories.
   ```bash
   du -sh /path/to/directory
   ```

4. **System Monitoring**:
   - **`top`** - Displays real-time system processes and resource usage.
   - **`htop`** - Enhanced version of `top` (requires installation).
   - **`free -h`** - Shows memory usage in human-readable format.

---

## Process Management

1. **`ps`** - Lists running processes.
   ```bash
   ps aux     # List all processes with details
   ```

2. **`kill`** - Terminates a process by ID.
   ```bash
   kill PID   # Replace PID with the actual Process ID
   ```

3. **`pkill`** - Terminates processes by name.
   ```bash
   pkill process_name
   ```

4. **Job Control**:
   - **`bg`** - Backgrounds a job.
   - **`fg`** - Brings a job to the foreground.

---

## Permissions Management

1. **`chmod`** - Changes file permissions.
   ```bash
   chmod +x filename.sh     # Adds execute permission
   chmod 755 filename.txt   # Set specific permissions
   ```

2. **`chown`** - Changes file owner and group.
   ```bash
   chown user:group filename.txt
   ```

**Tip**: Use `chmod -R` to change permissions recursively on all files within a directory.

---

## Networking Essentials

1. **`ping`** - Checks connectivity to another network host.
   ```bash
   ping google.com
   ```

2. **`ifconfig`** - Displays network interfaces and their details (try `ip a` for newer distros).

3. **`netstat`** - Shows network connections, routing tables, etc.

4. **`curl`** - Transfers data to or from a server.
   ```bash
   curl http://example.com
   ```

---

## Shell Scripting Basics

A shell script automates tasks. Here’s a quick example:

1. Create a file called `greet.sh`:
   ```bash
   nano greet.sh
   ```

2. Add the following code:
   ```bash
   #!/bin/bash
   echo "Hello, $USER! Today is $(date)."
   ```

3. Make it executable:
   ```bash
   chmod +x greet.sh
   ```

4. Run the script:
   ```bash
   ./greet.sh
   ```

**Tip**: Use `$(command)` syntax to run commands within a script.

---

## Pro Tips and Tricks

1. **Alias Common Commands**:
   - Save time by creating command aliases.
   ```bash
   alias ll='ls -la'     # Long listing with hidden files
   alias gs='git status' # Git status shortcut
   ```

2. **Quick Directory Navigation**:
   - Use `pushd` and `popd` to manage directory stacks, allowing you to quickly return to previous directories.

3. **Using `find` to Locate Files**:
   ```bash
   find /path -name "*.txt"     # Find all .txt files
   ```

4. **Piping and Redirection**:
   - Use `|` to pipe output from one command to another.
   ```bash
   ps aux | grep 'python'       # Filter processes for 'python'
   ```

5. **Command Substitution for Efficiency**:
   - Embed one command's output within another using `$()`.
   ```bash
   echo "There are $(ls | wc -l) files in this directory."
   ```

6. **Checking Command History**:
   ```bash
   history | grep 'command'     # Search command history
   ```

7. **Keyboard Shortcuts**:
   - **`Ctrl + C`** - Cancel current command.
   - **`Ctrl + Z`** - Suspend current job.
   - **`Ctrl + R`** - Search command history.

---

## Connect with Me

Feel free to connect with me on my other platforms for updates, queries, or collaborations!

- GitHub: [Srijan Paul](https://github.com/paul-srijan)
- LinkedIn: [Srijan Paul](https://www.linkedin.com/in/srijan-paul-547354260/)

---


## Additional Resources

- [Linux Command Line Basics - Official Documentation](https://tldp.org/LDP/intro-linux/html/index.html)
- [Linux Man Pages](https://man7.org/linux/man-pages/)
- [Shell Scripting Guide](https://www.shellscript.sh/)
- [ExplainShell](https://explainshell.com/) - Explains shell commands and syntax.

---

Happy learning, and enjoy mastering the Linux command line!