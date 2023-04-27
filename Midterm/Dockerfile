FROM python 

RUN apt-get update
# RUN yum update -y && \ yum install -y python3
RUN pip3 install pytest==7.0.0

# Copy code from python file to docker
COPY ISS_midtem.py /root/ISS_midterm.py
# COPY XMLsightingUSA.xml /root/sighting.xml
# COPY ISS.OEM_J2K_EPH.xml /root/position.xml

# Run code
# RUN chmod +rx /root/ISS_midtem.py


# CMD [“echo”, “Initalizing python script”]
# Command to start python script
CMD ["python3", "ISS_midterm.py"]