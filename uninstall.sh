#!/bin/bash

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' 

echo -e "${GREEN}[*] Uninstalling Hashfang...${NC}"

SYMLINK_PATH="/usr/local/bin/hashfang"

# Check if the symlink exists
if [ -L "$SYMLINK_PATH" ]; then
    echo -e "${GREEN}[*] Removing global 'hashfang' command...${NC}"
    echo -e "${GREEN}[*] This may require your password for sudo access.${NC}"
    
    if sudo rm "$SYMLINK_PATH"; then
        echo -e "${GREEN}[+] Successfully uninstalled Hashfang from system path.${NC}"
    else
        echo -e "${RED}[!] Failed to remove symbolic link. Please check your permissions.${NC}"
        exit 1
    fi
else
    echo -e "${RED}[!] Hashfang is not installed in $SYMLINK_PATH or it is not a symbolic link.${NC}"
fi

echo -e "${GREEN}[+] Uninstallation complete.${NC}"
echo -e "${GREEN}[*] Note: Dependencies installed via pip were not removed.${NC}"
echo -e "${GREEN}[*] You can now safely delete this directory.${NC}"