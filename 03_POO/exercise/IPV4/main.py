import re

class CalcIPv4:
    """
    Calculates IPv4 networks

    Mode of use 1:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', prefix=10)

    Mode of use 2:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', mask='255.255.255.0')
    """

    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

        if mask is None and prefix is None:
            raise ValueError('Need to send mask or prefix')

        if mask and prefix:
            raise ValueError('Need to send mask or prefix, not both.')

        self._set_broadcast()
        self._set_network()

    @property
    def network(self):
        return self._network

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numberIps(self):
        return self._get_numberIps()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mark

    @property
    def prefix(self):
        if self._prefixo is None:
            return

        return self._prefixo

    @ip.setter
    def ip(self, value):
        if not self._validate_ip(value):
            raise ValueError('IP invalid.')

        self._ip = value
        self._ip_bin = self._ip_to_bin(value)

    @mask.setter
    def mask(self, value):
        if not value:
            return

        if not self._validate_ip(value):
            raise ValueError('invalid mask.')

        self._mark = value
        self._mark_bin = self._ip_to_bin(value)

        if not hasattr(self, 'prefix'):
            self.prefix = self._mark_bin.count('1')

    @prefix.setter
    def prefix(self, value):
        if value is None:
            return

        try:
            value = int(value)
        except:
            raise ValueError('Prefix must be an integer.')

        if value > 32 or value < 0:
            raise TypeError('Prefix must be 32 bits.')

        self._prefixo = value
        self._mark_bin = (value * '1').ljust(32, '0')

        if not hasattr(self, 'mask'):
            self.mask = self._bin_to_ip(self._mark_bin)

    @staticmethod
    def _validate_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(bloco))[2:].zfill(8) for bloco in blocos]
        blocos_bin_str = ''.join(blocos_bin)
        qtd_bits = len(blocos_bin_str)

        if qtd_bits > 32:
            raise ValueError('IP or mask is more than 32 bits.')

        return blocos_bin_str

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefix
        self._broadcast_bin = self._ip_bin[:self.prefix] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_network(self):
        host_bits = 32 - self.prefix
        self._network_bin = self._ip_bin[:self.prefix] + (host_bits * '0')
        self._network = self._bin_to_ip(self._network_bin)
        return self._network

    def _get_numberIps(self):
        return 2 ** (32 - self.prefix)


def main():
    """ Exemplos de Uso """

    # Com prefix
    calc_ipv4_1 = CalcIPv4(ip='192.168.0.128', prefix=30)

    print(f'IP: { calc_ipv4_1.ip }')
    print(f'Mask: { calc_ipv4_1.mask }')
    print(f'Network: { calc_ipv4_1.network }')
    print(f'Broadcast: { calc_ipv4_1.broadcast }')
    print(f'Prefix: { calc_ipv4_1.prefix }')
    print(f'Number of network IPs: { calc_ipv4_1.numberIps }')

    print('#' * 80)

    # Com máscara
    calc_ipv4_2 = CalcIPv4(ip='192.168.0.128', mask='255.255.255.192')

    print(f'IP: { calc_ipv4_2.ip }')
    print(f'Mask: { calc_ipv4_2.mask }')
    print(f'Network: { calc_ipv4_2.network }')
    print(f'Broadcast: { calc_ipv4_2.broadcast }')
    print(f'Prefix: { calc_ipv4_2.prefix }')
    print(f'Number of network IPs: { calc_ipv4_2.numberIps }')


if __name__ == '__main__':
    main()
