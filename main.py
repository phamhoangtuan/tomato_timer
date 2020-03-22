import simpleaudio as sa
import time


class TomatoTimer():
    def __init__(
        self,
        pomodoro_minutes=None,
        short_break_minutes=None,
        long_break_minutes=None,
        target_pomodoro=None
    ):
        self.pomodoro_time = pomodoro_minutes if pomodoro_minutes else 25
        self.short_break_time = \
            short_break_minutes if short_break_minutes else 5
        self.long_break_time = long_break_minutes if long_break_minutes else 10
        self.target_pomodoro = target_pomodoro if target_pomodoro else 10

    def _countdown_and_print_log(self, minutes):
        seconds = minutes * 60
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            time_format = 'Remaining {:02d}:{:02d}'.format(mins, secs)
            print(time_format, end='\r')
            time.sleep(1)
            seconds -= 1
        self._play_sound()

    def _play_sound(self):
        print('Playing sound')
        file_name = 'sound.wav'
        wave_obj = sa.WaveObject.from_wave_file(file_name)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def start_pomodoro_phase(self):
        print('Start Pomodoro phase')
        self._countdown_and_print_log(self.pomodoro_time)
        print('Finish Pomodoro phase')

    def start_short_break_phase(self):
        print('Start Short break phase')
        self._countdown_and_print_log(self.short_break_time)
        print('Finish Short break phase')

    def start_long_break_phase(self):
        print('Start Long break phase')
        self._countdown_and_print_log(self.long_break_time)
        print('Finish Long break phase')

    def start_timer(self):
        print('Start Tomato timer')
        for i in range(1, self.target_pomodoro + 1):
            self.start_pomodoro_phase()
            if i % 4 == 0:
                self.start_long_break_phase()
            else:
                self.start_short_break_phase()
        print('Stop Tomato timer')


if __name__ == '__main__':
    timer = TomatoTimer()
    timer.start_timer()
