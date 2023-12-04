<a name="readme-top"></a>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](http://snf-880200.vm.okeanos.grnet.gr/randomizationservice/dashboard)

A simple web service for the randomization of patients prior to an Randomized Clinical Trial with the block randomization logic. The user can either randomize a single participant with a specific percentage allocation in mind or a list of participants, where the user also can choose the block size and the percentage allocation for each block.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built and Deployed With

* Flask
* Flask-RESTful
* Jinja2
* Nginx
* Gunicorn

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

The project is a python based webapp that uses Flask, Flask-RESTful and Jinja to generate randomized allocations for a single participant or a list based on the input values the user has provided. 

Use these instruction and Clone the repository locally (instructions below) and run it using the Flask build-in development server

### Prerequisites

* Make sure you have the latest version of Python installed.
* Make sure your system is up to date
  * In case you want to deploy it to a remote server, make sure the server and all its packages are upgraded to the latest versions
* (RECOMENDED) To deploy the app in a virtual enviroment 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/inab-certh/randomization-service.git
   ```
2. Install the required packages. All needed packages have been exported to the "requirements.txt" file
   ```sh
   pip install -r requirements.txt
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Running the Development server

* Clone the repo
   ```sh
   python __init__.py
   ```
* To view the app navigate to your browser to http://127.0.0.1:5000

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/randomizationFeature`)
3. Commit your Changes (`git commit -m 'Add some randomizationFeature'`)
4. Push to the Branch (`git push origin feature/randomizationFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments and References

We want to thank all the [MyPal](https://mypal-project.eu) consortium members that aided in the design and implementation of this service.

Also the present service has been presented in a Poster form at the Medical Informatics Europe 2021 (MIE2021). You can find it [Here](https://ebooks.iospress.nl/doi/10.3233/SHTI210375)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/template.png