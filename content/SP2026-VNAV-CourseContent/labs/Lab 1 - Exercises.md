---
title: "Lab 1 - Exercises"
tags:
  - vnav
  - labs
---

# Lab 1 - Exercises

> [!info] Related Lectures & Notes
> - [[CS4733_5733_F25_lecture1_Introduction.pdf_viewer|Lecture 1 - Introduction]]
> - [[CS4733_5733_Fall2025_Syllabus.pdf_viewer|Course Syllabus]]

> [!important] Submission Repository Requirement
> To submit your solutions, you are required to create a repository in the **OUVNAV2025** organization (this is your first exercise).
>
> **Important:** Ensure you create a **Private** repository for your submission in the **OUVNAV2025** organization. Otherwise, your submission will be visible to everyone.

> [!warning] Submission Deadline
> VNAV staff will clone your repository at the scheduled submission deadline to grade your submission. Please refer to Canvas / the course syllabus for exact due dates.
>
> **Late Submission:** We will assume your repository is ready to be graded at the deadline. Please email the staff if you need to submit after the deadline.

> [!note] Using AI Assistants (e.g. ChatGPT)
> If you use an AI assistant to complete your assignment, you must mention it explicitly in your submission.

### Exercises

### Git (5 pts)

In this exercise you are required to set a git repository inside the OUVNAV2025 organization. This is required for the correct submission of all the exercises of the class.

1. Create a repository for your personal submissions
  - Go to [https://github.com/organizations/OUVNAV2025/repositories/new](https://github.com/organizations/OUVNAV2025/repositories/new) to create a new repository.
  - Create a new**Private**repository and call it as your 4x4 at OU.
  - Clone the repository to a folder of your choice (e.g., `/vnav-individual), Note: `you will have a team repository later

```bash
git clone git@github.com:OUVNAV2025/YOUR_USERNAME.git -s ~/vnav-individual
```

(replace`YOUR_USERNAME`with the name of the repo you just created)

2. For downloading the codebase in this class, clone https://github.com/OUVNAV2025/labs.gitin
 a folder of your choice. Create a folder called lab1. You need to add 
your answer file in this folder and push it to the Github.

**It is 
important you create PRIVATE repository for your submission in 
OUVNAV2025 organization. Otherwise, your submission will be visible to 
everyone.**

> [!tip] SSH Key Setup
> You may need to create an SSH Key to clone your repository. Follow the instructions on [StackOverflow: How to solve permission denied (publickey)](https://stackoverflow.com/questions/2643502/git-how-to-solve-permission-denied-publickey-error-when-using-git).

> [!caution] Personal Account Warning
> If you created the repository under your personal account instead of **OUVNAV2025**, you must transfer ownership. Scroll to the bottom of the page for step-by-step instructions.

### Installing Ubuntu 24.04 (5 pts)

Please take a screenshot from your computer verifying you have Ubuntu
 24.04 installed on your system, called it ubuntu24, and push it in lab1
 repository. You may review the tutorial [here](https://canvas.ou.edu/courses/500928/pages/installing-ubuntu-24-dot-04). To print the Ubuntu version, you may run the following command in your terminal:

```bash
lsb_release -a
```

### ROS2Jazzy (5 Pts)

Please install ROS2Jazzy and upload the screenshot confirming you 
have a correct version of ROS installed in your system. You can find a 
tutorial [here](https://canvas.ou.edu/courses/500928/pages/tutorial-installing-ros2-jazzy). To print the ROS version, you may run the following command in your terminal:

```bash
echo $ROS_DISTRO
```

### Team assignment (5Pts)

Please confirm you have completed your team assignment. Please share your teammate and team number. **Note: Please fillout the team assignment as soon as possible to receive the robot.**

Shells (25 pts)

Exercise 1 - Answer to the following questions:

Download [https://raw.githubusercontent.com/dlang/dmd/master/druntime/benchmark/extra-files/dante.txt](https://raw.githubusercontent.com/dlang/dmd/master/druntime/benchmark/extra-files/dante.txt) (try using`wget`)

1. 
  - Create a file called`exercise1.txt`in`~/vnav-personal/lab1`and answer to the following questions
    1. How many lines does it contains?
    2. How many words does it contains?
    3. How many lines are not blank?

  - Push the file to git

2. Exercise 2 - Output redirecting
  - Install`fortune-mod`using`apt`
  - After installation, type`fortune`in your terminal to see a (hopefully) interesting proverb/quote
  - Run`fortune`5 more times and each time redirect the output to a file called`fortunes.txt`in`~/vnav-personal/lab1`(Hint: do not recreate the file 5 times - each time a new proverb should be added to the end of`fortunes.txt`)
  - Push the file to git

> [!tip] Shell Hint
> For the first exercise, you might want to use the command `wc` (Word Count).

### C++: Warm-up Exercises (25 pts)

Feel free to refer to[this](https://en.cppreference.com/w/)when answering the following questions. Some of the questions below are based on[C++ Primer](https://www.oreilly.com/library/view/c-primer-fifth/9780133053043/), which is also an excellent resource for C++ programming. Put all answers into a text file called`cpp-warmup.txt`and push it to git. Make sure you create a folder lab1 and push your answers there. Otherwise, they may not be graded.

**Please make sure you explain your answers. Otherwise, you may lose some points.**

*Operators*

1. What are the values of`i`and`j`after running the following code? Explain.

```bash
i = 0, j;
j = ++i;
j = i++;
```
2. What does the following code print?

```cpp
int i = 42;
std::string output = (i < 42) ? "a" : "b";
std::cout << output << std::endl;
```

*References and Pointers*

3. What is the difference between `int* i and int& i?`

4. What does the following code print? Explain your answer

```cpp
int i;
int& ri = i;
i = 5;
ri = 10;
std::cout << i << " " << ri << std::endl;
```

5. What does the following code print? Explain your answer

```cpp
int i = 42;
int* j = &i;
*j = *j**j;
std::cout << *j << std::endl;
```

6. What does the following code print?

```cpp
int i[4] = {42,24,42,24};
*(i+2) = *(i+1)-i[3];
std::cout << *(i+2) << std::endl;
```

7. What does the following code print? Explain your answer

```cpp
void reset(int &i) {
    i = 0;
}

int j = 42;
reset(j);
std::cout << j << std::endl;
```

*Numbers*

8. What are the differences between a`float`and`double`? What is the value of`i`after running the following code snippet?

```cpp
int i;
i = 3.14;
```

9. What will the value of`i`be after running the following code snippet? Explain your answer

```cpp
int i = 42;
if (i) {
 i = 0;
} else {
 i = 43;
}
```

### C++: RandomVector (30 pts)

In this exercise we will implement the class`RandomVector`. Inside`~/vnav-personal/lab1`create a folder called`RandomVector`and copy the content from [https://github.com/airou-lab/OUVNAV2025-labs/tree/main/lab1](https://github.com/airou-lab/OUVNAV2024-labs/tree/main/lab1). (note: you may not have access to this repository unless you have provided your github account in the survey).

The class`RandomVector`defined in the header file`random_vector.h`abstract a vector of doubles. You are required to implement the following methods:

- `RandomVector(int size, double max_val = 1)`(constructor): initialize a vector of doubles of size`size`with random values between 0 and`max_val`(default value 1)
- `double mean()`returns the mean of the values in random vector
- `double max()`returns the max of the values in random vector
- `double min()`returns the min of the values in random vector
- `void print()`prints all the values in the random vector
- `void printHistogram(int bins)`computes the histogram of the values using`bins`number of bins between`min()`and`max()`and print the histogram itself (see the example below).

To do so complete all the`TODO`s in the file`random_vector.cpp`. When you are done compile the application by running

```bash
g++ -std=c++11 -Wall -pedantic -o random_vector main.cpp random_vector.cpp
```

**Note:**we expect you to not use the function from the`<algorithm>`header.

> [!success] Expected Output: RandomVector
> If you complete the exercise correctly, you should see output similar to:
> ```text
> $ ./random_vector
0.458724 0.779985 0.212415 0.0667949 0.622538 0.999018 0.489585 0.460587
 0.0795612 0.185496 0.629162 0.328032 0.242169 0.139671 0.453804 
0.083038 0.619352 0.454482 0.477426 0.0904966
Mean: 0.393617
Min: 0.0667949
Max: 0.999018
Histogram:
***     ***
***     ***
***     ***
***     ***
***     ***
***     ***
***     *** ***
*** *** *** *** ***
> ```

10. Take a screen shot, and push it/upload it in your lab1 
folder in Git repository. please call it random_vector_screenshot

## Transfer ownership of Git repository

If you created the repository in your personal account instead of OU*VNAV2025*you might want to transfer the ownership in order to complete your submission.

1. On GitHub, navigate to the main page of the repository.
2. Under your repository name, click**Settings**.

![TransferOwnershipStep1.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/transferownershipstep1.png)
3. Scroll down until your reach the**Danger Zone**, then click**Transfer**.

![TransferOwnershipStep2.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/transferownershipstep2.png)
4. Type the name of your repository in the first row and  OUVNAV2025-submissionsin the second, then click**I understand, transfer this repository**.

![TransferOwnershipStep3.png](https://airou-lab.github.io/general_wiki_website/sp2026-vnav-coursecontent/uploaded-media/transferownershipstep3.png)
5. Done!

---

**Next**: [[Lab 2 - Exercises|Lab 2: ROS 2 Basics, Coordinate Frames & TF ➔]]
