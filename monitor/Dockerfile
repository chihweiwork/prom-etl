FROM centos:7

# 安裝 SSH 相關套件
RUN yum -y update && \
    yum -y install openssh-server passwd && \
    yum -y install vim wget gcc g++ make cmake net-tools && \
    yum clean all

# 建立 SSH 用戶並設定密碼
# RUN useradd -rm -d /home/dockeruser -s /bin/bash -G root -u 1001 dockeruser && \
#     echo 'dockeruser:password' | chpasswd

# 啟用 SSH 服務
RUN ssh-keygen -A

# 啟用 root 登入 SSH
RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config

# 開放 SSH Port
EXPOSE 22

# 啟動 SSH 服務
CMD ["/usr/sbin/sshd", "-D"]

