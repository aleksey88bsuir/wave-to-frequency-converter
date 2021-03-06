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
    if start_receive_freq <= freq <= stop_receive_freq:
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
    if starting_transmitting_freq <= freq <= stopping_transmitting_freq:
        return freq
    else:
        return 'Проверьте номер волны, он задан неверно'

    
def convert_frequency_in_wave_number_when_transmitting(frequency:int, transponder:int):
    duplex_spacing = 2_325_000
    starting_transmitting_freq = 3_400_000 + duplex_spacing
    stopping_transmitting_freq = 3_900_000 + duplex_spacing
    if not (starting_transmitting_freq <= frequency <= stopping_transmitting_freq):
        return 'Проверьте частоту, он задана неверно'
    offset_freq = frequency - starting_transmitting_freq
    offset_wave = (offset_freq + 15000) / 10
    return int(offset_wave)

def convert_frequency_in_wave_number_when_receiving(frequency:int, transponder:int):
    start_receive_freq = 3_400_000
    stop_receive_freq = 3_900_000
    if not (start_receive_freq <= frequency <= stop_receive_freq):
        return 'Проверьте частоту, он задана неверно'
    offset_freq = frequency - start_receive_freq
    offset_wave = (offset_freq + 15000) / 10
    # offset_wave = wave - (5000*(transponder-1)+1500)
    rx_wave = offset_wave - (5000*(transponder-1)+1500)
    if int(rx_wave) > 5000 or int(rx_wave) < 0:
        return 'Проверьте частоту или номер ствола'
    return int(rx_wave)


if __name__ == "__main__":
    a = convert_wave_number_to_frequency_when_receiving(770, 4)
    # b = convert_wave_number_to_frequency_when_receiving(17270, 4)
    # print(a == b)
    # c = convert_wave_number_to_frequency_when_transmitting(770, 4)
    d = convert_wave_number_to_frequency_when_transmitting(17270, 4)
    # print(c)
    # print(d)
    # # print(d)
    # print(c == d)
    # e = convert_frequency_in_wave_number_when_transmitting(5725000, 4)
    # i = convert_frequency_in_wave_number_when_receiving(3900000, 10)
    print (convert_frequency_in_wave_number_when_receiving(a, 4))
    print (convert_frequency_in_wave_number_when_transmitting(d, 4))