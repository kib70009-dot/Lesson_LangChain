# Lesson_LangChain
LangChain
### 上課連結
  https://meet.google.com/itw-ewsf-fum

## 上課安裝軟體
###步驟1.安裝編輯器
	cursor
###步驟2.安裝擴充套件
	1.chinese
	2.python
	3.jupyter_notebook
###步驟3. 安裝git
	1.建立Git帳號
	2.建立本機端Clone資料夾
	3.cursor終端機執行下列指令
		１．git config --global user.name "帳號"
		２．git config --global user.email "ＥＭＡＩＬ帳號"
		３．git config --global pull.rebase false
	4.cursor指定clone資料夾
###步驟4. 安裝mini-condaconda基本設定和基本指令
	1.安裝mini-conda
	2.取消termail一開始就進入base虛擬環境
		conda config --set auto_activate_base false
	3.conda init
		conda init --all bash
	4.conda版本檢查
		conda -V
	5.conda更新
		conda update conda
	6.檢查目前已建立的虛擬環境
		conda env list
	7.建立虛擬環境
		conda create --name 虛擬環境名 python=3.11(版本)
	8.啟動虛擬環境
		conda activate 虛擬環境名
	9.離開虛擬環境
		conda deactivate
	10.安裝套件
		conda activate 虛擬環境名
	11.conda install matplotlib
		conda install --name 虛擬環境名 matplotlib
	12.安裝requirement.txt
		conda install --yes --file requirements.txt
	13.檢查目前安裝的套件
		conda list
	14.刪除虛擬環境
		conda env remove --name 虛擬環境名
	15.刪除虛擬環境的套件
		conda remove --name 虛擬環境名 matplotlib
###步驟5. 本機安裝ollama
	1.ollama --version
	2.下載模型
		ollama pull llama3.2:3b
	3.檢視目前已經下載的模型
		ollama list
	4.執行模型
		ollama run llama3.2
	5.停止執行模型
		>>> /bye
	6.目前被載入的模型
		ollama ps
	7.停止模型
		ollama stop llama3.2
	8.刪除模型
		ollama rm llama3.2