import os
import shutil
import tempfile
import subprocess
import filecmp

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
MYCVS = SOURCE_DIR + '/mycvs.py'

def start_test():
    TEST_DIR = tempfile.mkdtemp()
    os.chdir(TEST_DIR)


def end_test():
    pass


def test_init_creates_directory_mycvs_if_not_existed():
    start_test()

    init = subprocess.Popen('python3 ' + MYCVS + ' init ' + 'mycvs', stdout=subprocess.PIPE, shell=True)
    out, err = init.communicate()
    if os.path.isdir('mycvs'):
        print('Test passed')
    else:
        print('Test failed')

    end_test()

def test_init_creates_directory_mycvs_if_existed():
    start_test()

    os.mkdir('mycvs')
    init = subprocess.Popen('python3 ' + MYCVS + ' init ' + 'mycvs', stdout=subprocess.PIPE, shell=True)
    out, err = init.communicate()
    
    if out == b"This project already exist\n":
        print('Test passed')
    else:
        print('Test failed')

    end_test()

def test_commit_creates_directory_and_file_if_info_file_existed():
    start_test()

    os.mkdir('mycvs')
    os.chdir('mycvs')
    main_file = open('main.py', 'w').close()
    info_file = open('info.txt', 'w')
    info_file.write('0')
    info_file.close()
    commit = subprocess.Popen('python3 ' + MYCVS + ' commit', stdout=subprocess.PIPE, shell=True)
    out, err = commit.communicate()
    if os.path.isdir('v1'):
        print('Test passed')
    else:
        print('Test failed')

    end_test()

def test_commit_creates_directory_and_file_if_info_file_not_existed():
    start_test()

    os.mkdir('mycvs')
    os.chdir('mycvs')
    main_file = open('main.py', 'w').close()
    commit = subprocess.Popen('python3 ' + MYCVS + ' commit', stdout=subprocess.PIPE, shell=True)
    out, err = commit.communicate()
    if out == b'Info file is missing\n':
        print('Test passed')
    else:
        print('Test failed')

    end_test()

def test_commit_creates_directory_and_file_if_info_file_is_corrupted():
    start_test()

    os.mkdir('mycvs')
    os.chdir('mycvs')
    main_file = open('main.py', 'w').close()
    info_file = open('info.txt', 'w')
    info_file.write('random text')
    info_file.close()
    commit = subprocess.Popen('python3 ' + MYCVS + ' commit', stdout=subprocess.PIPE, shell=True)
    out, err = commit.communicate()
    if out == b'Info file is corrupted\n':
        print('Test passed')
    else:
        print('Test failed')

    end_test()

def test_commit_creates_directory_and_file_if_directory_allready_exist():
    start_test()

    os.mkdir('mycvs')
    os.chdir('mycvs')
    os.mkdir('v1')
    main_file = open('main.py', 'w').close()
    info_file = open('info.txt', 'w')
    info_file.write('0')
    info_file.close()
    commit = subprocess.Popen('python3 ' + MYCVS + ' commit', stdout=subprocess.PIPE, shell=True)
    out, err = commit.communicate()
    if out == b'This version already exist\n':
        print('Test passed')
    else:
        print('Test failed')

    end_test()

def test_checkout_if_checkout_version_exict():
    start_test()

    os.mkdir('mycvs')
    os.chdir('mycvs')
    main_file = open('main.py', 'w')
    main_file.write('random text v0')
    main_file.close()
    os.mkdir('v1')
    main_file = open('v1/main.py', 'w')
    main_file.write('random text v1')
    main_file.close()
    commit = subprocess.Popen('python3 ' + MYCVS + ' checkout ' + 'v1', stdout=subprocess.PIPE, shell=True)
    out, err = commit.communicate()
    if filecmp.cmp('main.py', 'v1/main.py'):
        print('Test passed')
    else:
        print('Test failed')

    end_test()

def test_checkout_if_checkout_version_not_exict():
    start_test()

    os.mkdir('mycvs')
    os.chdir('mycvs')
    main_file = open('main.py', 'w')
    main_file.write('random text v0')
    main_file.close()

    commit = subprocess.Popen('python3 ' + MYCVS + ' checkout ' + 'v1', stdout=subprocess.PIPE, shell=True)
    out, err = commit.communicate()
    if out == b'This version is missing\n':
        print('Test passed')
    else:
        print('Test failed')

    end_test()    
    
test_init_creates_directory_mycvs_if_not_existed()
test_init_creates_directory_mycvs_if_existed()
test_commit_creates_directory_and_file_if_info_file_existed()
test_commit_creates_directory_and_file_if_info_file_not_existed()
test_commit_creates_directory_and_file_if_info_file_is_corrupted()
test_commit_creates_directory_and_file_if_directory_allready_exist()
test_checkout_if_checkout_version_exict()
test_checkout_if_checkout_version_not_exict()
