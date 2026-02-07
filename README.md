# doi2clip
This utility extracts the information the provided doi, giving the formatted citation in BibTeX-like format. **The output is automatically copied to the clipboard**. 
Supported classes:
  - `article`
  - `inproceedings`

Feel free to request the implementation of new classes, as they will be added.

## Installation
Clone the repository:

```
git clone https://github.com/Maskul93/doi2clip.git
```

Install it:

```
pip install -e path/to/doi2clip
```

## Usage
```
doi2clip 10.XXXXX
```
```
doi2clip https://doi.org/10.XXXXX
```

### Example
```
doi2clip 10.1109/TNSRE.2025.3594540
```

It copies the following output to your clipboard and returns:

```
@article{Mascia2025,
	title = {Rotational Power: A New Accelerometer-Derived Metric to Assess Functional Impairment in Multiple Sclerosis},
	volume = {33}, 
	ISSN = {1558-0210},
	url = {http://dx.doi.org/10.1109/TNSRE.2025.3594540},
	DOI = {10.1109/tnsre.2025.3594540}, 
	journal = {IEEE Transactions on Neural Systems and Rehabilitation Engineering},
	publisher = {Institute of Electrical and Electronics Engineers (IEEE)},
	author = {Mascia, Guido and Meyer, Brett M. and Cherian, Josh and Kairamkonda, Dheeraj D. and Fanning, Jason and Rice, Paige E. and Sosnoff, Jacob J. and Solomon, Andrew J. and McGinnis, Ellen W. and McGinnis, Ryan S.}, 
	year = {2025}, 
	month = {},
	pages = {3096-3104} 
}
```
## License
This software is relesed under the GNU/GPL 3.0 License. 

## Contacts
Guido Mascia, mascia.guido@gmail.com, guidomascia.blog
