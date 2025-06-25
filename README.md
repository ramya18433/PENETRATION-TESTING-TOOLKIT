# PENETRATION-TESTING-TOOLKIT

*company : CODETECH IT SOLUTION

*NAME* : Meesala Ramya

*INTERN ID * : CT04DF610

*DOMAIN * :CYBER SECURITY AND ETHICAL HACKING 

DURATION  : 4 WEEKS 

MENTER  : NEELA SANTOSH

## PENETRATION-TESTING-TOOLKIT

This project is a Python-based modular penetration testing toolkit designed for educational and ethical hacking purposes. The toolkit integrates multiple essential functions used by penetration testers, such as a port scanner and a basic brute-force password attacker. The primary goal of this toolkit is to provide a simple, easy-to-use platform for beginners and cybersecurity students to understand and experiment with common penetration testing techniques using Python.

The toolkit is developed with a modular structure, making it highly extensible and adaptable for future improvements. Each feature is implemented as a separate function within the script, allowing users to easily add new tools or modify existing ones according to their requirements. Currently, the toolkit consists of two main modules: a port scanner and a brute-force attacker for web login forms. The port scanner allows users to scan common TCP ports on a target IP or domain to identify which services are open and potentially vulnerable. It uses Python’s built-in socket library to send TCP connection requests to popular ports such as 21, 22, 23, 80, 443, and 8080. Open ports can often reveal information about running services, giving attackers a possible entry point if vulnerabilities exist.

The second module is a basic brute-force password attacker designed to target web login forms. Using the requests library and the POST method, the script sends multiple login attempts with different password combinations to the target website. For demonstration purposes, the password list is predefined within the script, but it can be extended or replaced with external wordlists as needed. This type of brute-force attack is common during penetration testing to assess the strength of password protections on web applications. It is important to emphasize that this toolkit is for educational use only and should never be used on unauthorized targets.

One of the key advantages of this toolkit is its simplicity. The code is written in a clean, beginner-friendly format that is easy to read, understand, and modify. It provides new learners with an excellent opportunity to explore the basics of network scanning and web-based attacks without requiring complex tools or frameworks. The interactive command-line interface prompts users to select which module they want to run, enter relevant target information, and view the output directly within the terminal.

In the future, additional modules such as vulnerability scanners, directory brute-forcers, or even basic exploit tools can be incorporated into the same toolkit structure. This makes the project highly scalable for anyone interested in advancing their ethical hacking skills.

In conclusion, this Python-based penetration testing toolkit offers an excellent foundation for understanding the basic techniques used by security professionals. By practicing with this toolkit in legal environments such as personal lab setups or authorized platforms, learners can build confidence and technical skills needed for more advanced penetration testing and cybersecurity tasks. It serves as a stepping stone for anyone looking to explore the world of ethical hacking in a responsible, educational, and hands-on manner.

## CMD Port Scan Output
![Image](https://github.com/user-attachments/assets/d903c2c9-a3c8-4b90-868b-466f3d1b916e)

## Brute-Force Demo
![Image](https://github.com/user-attachments/assets/754ce0fd-966b-4495-b84a-953080ccfc28)
