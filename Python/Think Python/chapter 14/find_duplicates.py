import os
import re

def find_duplicate(directory, suffix, files=[], duplicates=[]):
    
    def is_duplicate(file1, file2):
        cmd = 'diff "%s" "%s"' % (file1, file2)
        fp = os.popen(cmd)
        res = fp.read()
        fp.close()
        return True if len(res) == 0 else False

    pattern = re.compile('.%s$'%suffix)
    top_dir = os.walk(directory)
    
    for direct in top_dir:
        for file in direct[2]:
            if re.search(pattern, file):
                file_abs_path = os.path.join(os.path.abspath(direct[0]), file)
                if len(files) == 0:
                    files.append((file, file_abs_path))
                else:
                    gen_files_path = (check_file[1] for check_file in files)
                    try:
                        dup_flag = False
                        for f in gen_files_path:
                            if is_duplicate(file_abs_path, f):
                                duplicates.append(('is duplicate of %s'%f[-9:],file_abs_path, file))
                                dup_flag = True
                                break
                        if not dup_flag:
                            files.append((file_abs_path, file))
                    except StopIteration:
                        continue
                    except:
                        print('Unexpected Error occured')
    return duplicates
if __name__ == '__main__':
    direct = './'
    suffix = '.dat'
    print('testing with dir', direct+' and suffix',suffix, sep = '\t>>>')
    print('duplicates are:',find_duplicate(direct,suffix),sep='\n\t>>>')