# scannet
Python loading functions for [ScanNet dataset](http://www.scan-net.org/).

## Getting the data
1. Set your `SCANNET_PATH` environment variable
```
export SCANNET_PATH=/path/to/scannet_data_dir
```
2. Use [this repository](http://www.cvlibs.net:3000/ageiger/rob_devkit/src/master) to download the segmentation data.
```
git clone http://cvlibs.net:3000/ageiger/rob_devkit.git
cd rob_devkit/segmentations
python download_scannet.py -o $SCANNET_PATH --type _vh_clean_2.labels.ply
```
3. Get non-pip dependencies
```
cd /path/to/parent_dir
export PYTHONPATH=$PYTHONPATH:/path/to/parent_dir
git clone https://github.com/jackd/dids.git
git clone https://github.com/jackd/util3d.git
git clone https://github.com/jackd/scannet.git
```
4. Install pip dependencies
```
pip install numpy plyfile
```
5. (Optional) Add export lines used above to your `~/.bashrc` file if you don't want to run them for each new terminal
```
export PYTHONPATH=$PYTHONPATH:/path/to/parent_dir
export SCANNET_PATH=/path/to/scannet_data_dir
```
