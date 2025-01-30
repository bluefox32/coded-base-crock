import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
fs = 1000  # サンプリング周波数（Hz）
T = 1      # 1秒間
f = 50     # 生成する信号の周波数（Hz）

# 時間軸を作成
t = np.linspace(0, T, fs * T, endpoint=False)

# 正弦波（サイン波）を生成
signal = np.sin(2 * np.pi * f * t)

# 波形をプロット
plt.plot(t, signal)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Generated Sine Wave (50 Hz)")
plt.grid()
plt.show()

from scipy.fftpack import fft

# FFT解析
fft_result = fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/fs)

# 正の周波数成分のみ表示
plt.plot(freqs[:len(freqs)//2], np.abs(fft_result)[:len(freqs)//2])
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.title("FFT of Generated Sine Wave")
plt.grid()
plt.show()