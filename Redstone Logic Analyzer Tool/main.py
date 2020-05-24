from logic_analyzer.screen import Screen
from logic_analyzer.timing_collector import TimingCollector
from logic_analyzer.text_loader import TextLoader
from sys import argv
import logging

logging.basicConfig(
	filename = '.\\log.txt',
	level = logging.DEBUG,
	filemode = 'w',
	format = '%(levelname)s - %(message)s'
)

log = logging.getLogger()

log_address = argv[1]
text_loader = TextLoader(log_address)
timing_collector = TimingCollector(text_loader)
signals = timing_collector.get_raw_info()
visible_signals = [
	"Reset",
	"State Machine Clock",
	"Input Ready",
	"State Machine State",
	"Phi1 Clock",
	"Phi2 Clock",
	"Program Counter Reset",
	"Program Counter Write",
	"Program Counter Increment",
	"Program Counter"
]
for signal in signals:
	if signal.name in visible_signals:
		visible_signals[visible_signals.index(signal.name)] = signal
screen = Screen()
render = screen.render(visible_signals)
render.save('.\image.png')