'''
Author: Lugy
Date: 2025-04-21 09:48:18
LastEditTime: 2025-04-21 10:00:58
LastEditors: Lugy
Description: 
版权声明
'''
import socket
import os
import shutil


def receive_images_from_server(server_host, server_port, save_folder):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    for i in range(10):
        # Receive the size of the image
        image_size_data = client_socket.recv(4)
        if not image_size_data:
            break
        image_size = int.from_bytes(image_size_data, 'big')

        # Receive the image data
        image_data = b''
        while len(image_data) < image_size:
            packet = client_socket.recv(image_size - len(image_data))
            if not packet:
                break
            image_data += packet

        # Save the image to the specified folder
        image_path = os.path.join(save_folder, f'image_{i+1}.jpg')
        with open(image_path, 'wb') as img_file:
            img_file.write(image_data)
        print(f"Received and saved {image_path}")

    client_socket.close()

if __name__ == "__main__":
    SERVER_HOST = '172.168.3.70'
    SERVER_PORT = 65432
    SAVE_FOLDER = 'dataset/CUHK-PEDES'  # Replace with the path to your save folder
    
    try:
        shutil.rmtree(SAVE_FOLDER)
        print(f"Deleted directory {SAVE_FOLDER}")
    except Exception as e:
        print(f"Error deleting directory {SAVE_FOLDER}: {e}")

    os.makedirs(SAVE_FOLDER, exist_ok=True)
    receive_images_from_server(SERVER_HOST, SERVER_PORT, SAVE_FOLDER)