Usage:
python extractor.py <masscan_logfile_name>
Example: python extractor.py masscan.log

Output in the "out.log" file in format:
IP:[list of open ports]

*Every line represents an IP:Port Combination 

You can additionally:
1: Put hosts and open ports as different text files named after hosts.
2: Write hosts to a file which have port 80 and 443 open (for httprobe).
3: Run nmap for service discovery and save results under the text file named after the hosts.
