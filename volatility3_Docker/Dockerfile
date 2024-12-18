# Volatility 3, on Docker 🐳

FROM alpine:latest

# Variables d'installation
ENV SYM_DIR="/usr/local/lib/volatility3/volatility3/symbols"
ENV PLUGINS_DIR="/usr/local/lib/volatility3/volatility3/plugins"
ENV VOL_REPO="https://github.com/volatilityfoundation"
ENV SYM_REPO="https://downloads.volatilityfoundation.org/volatility3/symbols"
ENV YARA_REPO="https://github.com/VirusTotal"
ENV TAB_REPO="https://github.com/JPCERTCC"

# Mettre à jour les paquets et installer les dépendances de base
RUN apk add --no-cache \
        curl make gcc bat git unzip less capstone dumb-init \
        py3-capstone py3-pefile py3-pip py3-pycryptodome py3-pygit2 python3 \
        linux-headers libusb-dev musl-dev python3-dev py3-setuptools

# Créer un environnement virtuel Python
RUN python3 -m venv /venv

# Préparer un répertoire de travail
VOLUME /tmp /var/tmp
RUN mkdir -p ~/temporaire

# Cloner Volatility 3 et installer les dépendances Python
RUN . /venv/bin/activate && pip install --upgrade pip setuptools wheel \
    && git clone --branch stable --depth 1 ${VOL_REPO}/volatility3 /usr/local/lib/volatility3 \
    && cd /usr/local/lib/volatility3 \
    && pip3 install --no-cache-dir -r requirements.txt \
    && python3 setup.py install

# Cloner les autres dépendances
RUN git clone --branch=main   --depth=1   --single-branch ${TAB_REPO}/Windows-Symbol-Tables.git ~/temporaire/symbols
RUN git clone --branch=master --recursive --single-branch ${YARA_REPO}/yara-python /yara-python
# RUN cd ${PLUGINS_DIR}/ && git clone --branch=master --depth=1 --single-branch ${VOL_REPO}/community3.git

RUN cp -r ~/temporaire/symbols/symbols/windows ${SYM_DIR}/windows && rm -rf ~/temporaire/symbols

# RUN cp -r ~/temporaire/community3/* ${PLUGINS_DIR} && rm -rf ~/temporaire/community3

# Télécharger les symboles
RUN curl --location --max-redirs 1 \
        ${SYM_REPO}/windows.zip -o ${SYM_DIR}/windows.zip \
        ${SYM_REPO}/linux.zip -o ${SYM_DIR}/linux.zip \
        ${SYM_REPO}/mac.zip -o ${SYM_DIR}/mac.zip \
        ${SYM_REPO}/SHA256SUMS -o ${SYM_DIR}/symbols.sha256 && \
    cd ${SYM_DIR} && sha256sum -c ${SYM_DIR}/symbols.sha256 && \
    find ${SYM_DIR} -type d -exec chmod 0777 "{}" \; && \
    find ${SYM_DIR} -type f -exec chmod 0666 "{}" \;

# Installer Yara-Python
RUN cd /yara-python \
    && python3 setup.py build \
    && find . -type d -exec chmod 0755 "{}" \; && find . -type f -exec chmod 0644 "{}" \;

# Créer des liens symboliques pour Volatility 3
RUN chmod 0755 /usr/local/lib/volatility3/vol.py /usr/local/lib/volatility3/volatility3/framework/symbols/windows/pdbconv.py \
    && for destination in "v3" "vol" "vol3" "volatility" "volatility3"; do \
        ln -sf /usr/local/lib/volatility3/vol.py /usr/local/bin/${destination}; \
    done && \
    ln -sf ${SYM_DIR}framework/symbols/windows/pdbconv.py /usr/local/bin/pdbconv

RUN rm -rf ~/temporaire

RUN echo "=== ls /home/ ===" && ls -la /home/

RUN volatility3 -vvv frameworkinfo.FrameworkInfo && \
    mkdir -p /home/.cache/volatility3 && \
    cp ~/.cache/volatility3/identifier.cache /home/.cache/volatility3/

# Point d'entrée pour exécuter Volatility 3
ENTRYPOINT ["/usr/bin/dumb-init", "--", "volatility3"]
CMD ["--help"]