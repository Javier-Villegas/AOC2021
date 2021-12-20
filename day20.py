from timeit import default_timer as timer
import numpy as np

def denoise(img,e_alg):
    ki = [-1,0,1]
    kj = [-1,0,1]
    new_img = np.zeros((img.shape[0]+2,img.shape[1]+2),dtype=int)
    new_img = new_img+int(e_alg[-1]=='#') if img[0,0] else new_img+int(e_alg[0]=='#')
    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
            code = 0
            for k_i in range(3):
                for k_j in range(3):
                    if img[i+ki[k_i],j+kj[k_j]]:
                        code += 2**(8-(k_i*3+k_j))
            new_img[i+1,j+1] = e_alg[code]=='#'
    return new_img

if __name__=='__main__':
    start = timer()

    with open('inputs/day20.txt','r') as f:
        pixels = f.readlines()
    e_alg = list(pixels[0][:-1])
    img = np.zeros((len(pixels[2:])+4,len(pixels[2][:-1])+4),dtype=int)

    img[2:-2,2:-2] = [[x=='#' for x in y[:-1]] for y in pixels[2:]]
    for _ in range(2):
        img = denoise(img,e_alg)

    print(f'Result part 1: {img.sum()}')
    for _ in range(48):
        img = denoise(img,e_alg)
    print(f'Result part 2: {img.sum()}')
    print(f'Elapsed time: {timer()-start} seconds')
