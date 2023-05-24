import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit

class WebFingerprint(QWidget):
    def _init_(self):
        super()._init_()
        
        # Set window properties
        self.setWindowTitle('Web Server Fingerprint Tool')
        self.setGeometry(100, 100, 500, 400)
        self.setStyleSheet("background-color:pink;")
        # Create input fields and button
        self.url_label = QLabel('ENTER THE URL:')
        self.url_label.setStyleSheet("border :3px solid black;")
        self.url_input = QLineEdit()
        self.url_input.setStyleSheet("background-color:purple;")
        self.url_input.setStyleSheet("border : 3px solid black")
  
        self.method_label = QLabel('HTTP Method:')
        self.method_label.setStyleSheet("border : 3px solid black")
        self.method_input = QComboBox()
        self.method_input.setStyleSheet("background-color:white;border:3px solid black")
        self.method_input.addItems(['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
        self.submit_button = QPushButton('Submit')
        self.submit_button.setStyleSheet("background-color:green;border : 3px solid black")
        self.submit_button.clicked.connect(self.do_fingerprinting)
        
        # Create output field
        self.output_label = QLabel('Output:')
        self.output_label.setStyleSheet("border : 3px solid black")
        self.output_field = QTextEdit()
        self.output_field.setStyleSheet("border : 2px solid black")

        self.output_field.setReadOnly(True)
        
        # Create layout
        self.input_layout = QVBoxLayout()
        self.input_layout.addWidget(self.url_label)
        self.input_layout.addWidget(self.url_input)
        self.input_layout.addWidget(self.method_label)
        self.input_layout.addWidget(self.method_input)
        self.input_layout.addWidget(self.submit_button)
        
        self.output_layout = QVBoxLayout()
        self.output_layout.addWidget(self.output_label)
        self.output_layout.addWidget(self.output_field)
        
        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.output_layout)
       
        
    
        self.setLayout(self.main_layout)
    
    def do_fingerprinting(self):
        # Get input values
        url = self.url_input.text()
        method = self.method_input.currentText()
        
        # Send request to server
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        try:
            response = requests.request(method, url, headers=headers)
        except:
            self.output_field.setText('Error: Invalid URL or HTTP method.')
            return
        
        # Extract server information from response headers
        server = response.headers.get('Server')
        x_powered_by = response.headers.get('X-Powered-By')
        date=response.headers.get('Date')
        expires=response.headers.get('Expires')
        lenght=response.headers.get('Content-Length')
        type=response.headers.get('Content-Type')
        connection=response.headers.get('Connection')

    
        # Display results
        result = 'Server: {}\nX-Powered-By: {}\nDate: {}\n Expires:{}\nContent-Length:{}\nContent-Type:{}\nConnection:{}'.format(server, x_powered_by,date,expires,lenght,type,connection)
        self.output_field.setText(result)

# Create application and run
app = QApplication([])
fingerprint_tool = WebFingerprint()
fingerprint_tool.show()
app.exec_()