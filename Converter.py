def convert_wave_number_to_frequency_when_receiving(wave:int, transponder:int):
    start_receive_freq = 3_400_000
    stop_receive_freq = 3_900_000
    offset_wave = wave - (5000*(transponder-1)+1500)
    # print(f'{offset_wave=} first')
    if offset_wave > 0:
        offset_freq = wave * 10 - 15000
    else:
        offset_wave = wave + (5000*(transponder-1)+1500)
        offset_freq = offset_wave * 10 - 15000
    freq = start_receive_freq + offset_freq
    if start_receive_freq < freq < stop_receive_freq:
        return freq
    else:
        return 'Проверьте номер волны, он задан неверно'



def convert_wave_number_to_frequency_when_transmitting(wave:int, transponder:int):
    duplex_spacing = 2_325_000
    starting_transmitting_freq = 3_400_000 + duplex_spacing
    stopping_transmitting_freq = 3_900_000 + duplex_spacing
    offset_wave = wave - (5000*(transponder-1)+1500)
    # print(f'{offset_wave=} first')
    if offset_wave > 0:
        offset_freq = wave * 10 - 15000
    else:
        offset_wave = wave + (5000*(transponder-1)+1500)
        offset_freq = offset_wave * 10 - 15000
    freq = starting_transmitting_freq + offset_freq
    if starting_transmitting_freq < freq < stopping_transmitting_freq:
        return freq
    else:
        return 'Проверьте номер волны, он задан неверно'


if __name__ == "__main__":
    a = convert_wave_number_to_frequency_when_receiving(770, 4)
    b = convert_wave_number_to_frequency_when_receiving(17270, 4)
    print(a == b)
    c = convert_wave_number_to_frequency_when_transmitting(770, 4)
    d = convert_wave_number_to_frequency_when_transmitting(17270, 4)
    print(d)
    print(c == d)
