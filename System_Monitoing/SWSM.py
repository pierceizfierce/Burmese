from flask import Flask, render_template, Response
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import os

app = Flask(__name__)

# Function to get CPU utilization
def get_cpu_percent():
    return psutil.cpu_percent(interval=0.1)

# Function to get memory utilization
def get_memory_percent():
    return psutil.virtual_memory().percent

# Function to get GPU utilization (assuming NVIDIA GPU)
def get_gpu_percent():
    result = os.popen('nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader').read()
    return int(result.strip().split()[0]) if result else 0

# Function to get network utilization
def get_network_stats():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

# Function to generate and save a CPU utilization plot
def generate_cpu_plot():
    fig, ax = plt.subplots()
    ax.set_title('CPU Utilization (%)')
    ax.set_ylim(0, 100)
    ax.plot([get_cpu_percent()])
    fig.savefig('static/cpu_plot.png')

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html',
                           memory_percent=get_memory_percent(),
                           gpu_percent=get_gpu_percent(),
                           bytes_sent=get_network_stats()[0],
                           bytes_recv=get_network_stats()[1])

# Route to stream CPU utilization plot
@app.route('/cpu_plot.png')
def stream_cpu_plot():
    generate_cpu_plot()
    return send_image('cpu_plot.png')

# Function to send an image
def send_image(filename):
    return Response(open(f'static/{filename}', 'rb'), mimetype='image/png')

# Main function
if __name__ == '__main__':
    # Run the app on port 8080
    app.run(debug=True, port=8080)
