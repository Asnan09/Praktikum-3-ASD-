RESET = "\033[0m"
PINK = "\033[95m"
BLUE = "\033[94m"

class Barang:
    def __init__(self, id_barang, nama, harga, stok, kategori):
        self.id_barang = id_barang
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori
        self.next = None

class TokoBangunan:
    def __init__(self):
        self.head = None

    def tambah_barang_di_awal(self, barang):
        barang.next = self.head
        self.head = barang

    def tambah_barang_di_akhir(self, barang):
        if not self.head:
            self.head = barang
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = barang

    def tambah_barang_di_antara(self, barang, id_sebelumnya):
        if not self.head:
            print("Linked list kosong.")
            return
        current = self.head
        while current:
            if current.id_barang == id_sebelumnya:
                barang.next = current.next
                current.next = barang
                return
            current = current.next
        print(f"Tidak ditemukan barang dengan ID {id_sebelumnya}. Barang tidak ditambahkan.")

    def hapus_barang_di_awal(self):
        if not self.head:
            print("Linked list kosong.")
            return
        self.head = self.head.next

    def hapus_barang_di_akhir(self):
        if not self.head:
            print("Linked list kosong.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def hapus_barang_di_antara(self, id_sebelumnya):
        if not self.head:
            print("Linked list kosong.")
            return
        if self.head.id_barang == id_sebelumnya:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.id_barang == id_sebelumnya:
                current.next = current.next.next
                return
            current = current.next
        print(f"Tidak ditemukan barang dengan ID {id_sebelumnya}. Barang tidak dihapus.")

    def tampilkan_barang(self):
        current = self.head
        while current:
            print(f"ID: {current.id_barang}, Nama: {current.nama}, Harga: {current.harga}, Stok: {current.stok}, Kategori: {current.kategori}")
            current = current.next

    def quick_sort(self, attribute, order='ascending'):
        items = []
        current = self.head
        while current:
            items.append(current)
            current = current.next
        if attribute == 'id_barang':
            comparison_key = lambda x: x.id_barang
        elif attribute == 'nama':
            comparison_key = lambda x: x.nama
        else:
            print("Attribute not supported for sorting.")
            return
        
        reverse = order.lower() == 'descending'

        def partition(low, high):
            pivot = items[high]
            i = low - 1
            for j in range(low, high):
                if (comparison_key(items[j]) < comparison_key(pivot)) ^ reverse:
                    i += 1
                    items[i], items[j] = items[j], items[i]
            items[i + 1], items[high] = items[high], items[i + 1]
            return i + 1

        def quick_sort_util(low, high):
            if low < high:
                pi = partition(low, high)
                quick_sort_util(low, pi - 1)
                quick_sort_util(pi + 1, high)

        quick_sort_util(0, len(items) - 1)

        self.head = items[0]
        for i in range(len(items) - 1):
            items[i].next = items[i + 1]
        items[-1].next = None

# Inisialisasi toko dan tambahkan barang
toko = TokoBangunan()
toko.tambah_barang_di_akhir(Barang(1, "Cat Tembok", 50000, 100, "Cat"))
toko.tambah_barang_di_akhir(Barang(2, "Paku", 1000, 200, "Perkakas"))
toko.tambah_barang_di_akhir(Barang(3, "Semenn", 75000, 50, "Material Bangunan"))
toko.tambah_barang_di_akhir(Barang(4, "Bor", 75000, 50, "Perkakas"))

print(PINK + "Daftar Barang sebelum diurutkan:" + RESET)
toko.tampilkan_barang()
print(BLUE + "====================================================================================================" + RESET)


# Urutkan berdasarkan ID secara descending
toko.quick_sort('id_barang', order='descending')
print("\n" + PINK + "Daftar Barang setelah diurutkan berdasarkan ID secara descending:" + RESET)
toko.tampilkan_barang()
print(BLUE + "====================================================================================================" + RESET)

# Urutkan berdasarkan Nama secara ascending
toko.quick_sort('nama', order='ascending')
print("\n" + PINK + "Daftar Barang setelah diurutkan berdasarkan Nama secara ascending:" + RESET)
toko.tampilkan_barang()
print(BLUE + "====================================================================================================" + RESET)
