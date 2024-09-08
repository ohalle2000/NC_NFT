

def address_to_binary(address):
    """Convert a hexadecimal address to a 160-bit binary string."""
    address = address[2:]  # Remove '0x' prefix
    binary_string = bin(int(address, 16))[2:].zfill(160)
    return binary_string

def binary_to_image_parameters(binary_address):
    """Convert a binary string to parameters for drawing the image."""
    list_image = []
    for i in range(9):
        NoughtCross = int(binary_address[16*i])
        Red = 7 * int(binary_address[16*i+1:16*i+6], 2)
        Green = 7 * int(binary_address[16*i+6:16*i+11], 2)
        Blue = 7 * int(binary_address[16*i+11:16*i+16], 2)
        list_image.append((NoughtCross, Red, Green, Blue))
    return list_image

def create_nft(address):
    binary_address = address_to_binary(address)
    """Create an SVG XML representation from a binary address."""
    list_image = binary_to_image_parameters(binary_address)

    # Define SVG size and cell size
    image_size = 300
    cell_size = image_size // 3
    frame_thickness = 20

    # Frame color
    FrameRed = 3 * int(binary_address[144:150], 2)
    FrameGreen = 7 * int(binary_address[150:155], 2)
    FrameBlue = 7 * int(binary_address[155:], 2)

    # SVG XML header
    svg_header = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{image_size }" height="{image_size}" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="{image_size}" height="{image_size}" fill="none" stroke="rgb({FrameRed},{FrameGreen},{FrameBlue})" stroke-width="{frame_thickness}"/>'''

    # Add the cells to SVG
    svg_cells = ""
    for i in range(9):
        NoughtCross, Red, Green, Blue = list_image[i]
        color = f"rgb({Red},{Green},{Blue})"
        row, col = divmod(i, 3)
        x, y = col * cell_size, row * cell_size

        if NoughtCross == 1:
            # Draw cross
            svg_cells += f'''
            <line x1="{x + 13}" y1="{y + 13}" x2="{x + cell_size - 13}" y2="{y + cell_size - 13}" stroke="{color}" stroke-width="10"/>
            <line x1="{x + 13}" y1="{y + cell_size - 13}" x2="{x + cell_size - 13}" y2="{y + 13}" stroke="{color}" stroke-width="10"/>'''
        else:
            # Draw nought (circle)
            svg_cells += f'''
            <circle cx="{x + cell_size / 2}" cy="{y + cell_size / 2}" r="{cell_size / 2 - 13}" stroke="{color}" fill="none" stroke-width="10"/>'''

    # SVG XML footer
    svg_footer = '</svg>'

    # Combine all parts
    svg_content = svg_header + svg_cells + svg_footer
    return svg_content


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_nft', methods=['POST'])

def generate_nft():
    data = request.json
    address = data.get('address')
    svg_code = create_nft(address)
    return jsonify({'svg': svg_code})

if __name__ == '__main__':
    app.run(debug=True)
# Example usage
#address = "0x55Aeb6053F3E94C9b9A09f33669435E7Ef1BeAed"
#svg_xml = create_nft(address)
#print(svg_xml)
