import matplotlib.pyplot as plt

plt.figure(figsize=[21.0/2.54,29.7/2.54]) # Maße in inch!
plt.text(1.0, 10.0, 'Rechnungsbetrag:') # Koordinaten in inch!
plt.savefig('rechnung.pdf')
