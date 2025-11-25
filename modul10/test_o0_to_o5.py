from o0_to_o5 import *
from pytest import raises
import csv

def read_csv(filename):
    with open(filename, 'rt', encoding='utf8', newline='\n') as file:
        return list(csv.reader(file))

#####       O1 OPGAVER      #####
##### o1_1 ----- index of #####
def test_index_of():
    v = ['dk', 'se', 'no', 'gb']
    d = index_of(v)
    assert d['dk'] == 0
    assert d['se'] == 1
    assert d['no'] == 2
    assert d['gb'] == 3
    assert len(d) == 4
    assert list(d.keys()) == v

def test_1L_index_of():
    v = ['dk', 'se', 'no', 'gb']
    d = one_liner_index_of(v)
    assert d['dk'] == 0
    assert d['se'] == 1
    assert d['no'] == 2
    assert d['gb'] == 3
    assert len(d) == 4
    assert list(d.keys()) == v

##### o1_2 ----- mac_index_of #####
def test_mac_index_of():
    v = [
        (64, 3.2, 8, '00:1A:2B:3C:4D:5E'),
        (128, 2.8, 16, '00:1A:2B:3C:4D:5F'),
        (32, 3.5, 6, '00:1A:2B:3C:4D:60'),
        (256, 2.6, 32, '00:1A:2B:3C:4D:61'),
    ]
    d = mac_index_of(v)
    assert d['00:1A:2B:3C:4D:5E'] == 0
    assert d['00:1A:2B:3C:4D:5F'] == 1
    assert d['00:1A:2B:3C:4D:60'] == 2
    assert d['00:1A:2B:3C:4D:61'] == 3
    assert len(d) == 4
    #assert list(d.values()) == v
    assert list(d.values()) == [0, 1, 2, 3]

##### o1_3 ----- MAC INDEX_OF_EXPANDED
def test_mac_index_of_expanded():
    with raises(ValueError):
        some_mac_address = '00:1A:2B:3C:4D:5E'
        mac_index_of_expanded([(64, 3.2, 8, some_mac_address), (128, 2.8, 16, some_mac_address)])

##### ----- o2 opgaver ----- #####

##### o2_1 opgave #####
def test_username_index_of():
    former_employees = [
        ("Alice Andersen", "010190-1234", "aandersen", "2022-03-01"),
        ("Bob Hansen", "020278-5678", "bhansen", "2023-01-15"),
        ("Carla Jensen", "150385-9876", "cjensen", "2021-11-30"),
    ]
    
    d = username_index_of(former_employees)
    
    assert d["aandersen"] == 0
    assert d["bhansen"] == 1
    assert d["cjensen"] == 2
    assert len(d) == 3


def test_username_index_of_duplicate():
    with raises(ValueError):
        same_user = "dupuser"
        username_index_of([
            ("Test1", "000000-0000", same_user, "2020-01-01"),
            ("Test2", "111111-1111", same_user, "2021-01-01"),
        ])

##### o2_2 opgave #####
def test_post_termination_logins_of():
    former_employees = [
        ("Alice Andersen", "010190-1234", "aandersen", "2022-03-01"),
        ("Bob Hansen", "020278-5678", "bhansen", "2023-01-15"),
    ]

    auth_log = [
        ("server1", "2022-02-15", "aandersen", "SUCCESS"),  # før fratrædelse
        ("server1", "2022-03-05", "aandersen", "SUCCESS"),  # efter fratrædelse ✅
        ("server2", "2023-01-10", "bhansen", "FAIL"),       # før fratrædelse
        ("server2", "2023-01-20", "bhansen", "SUCCESS"),    # efter fratrædelse ✅
        ("server3", "2023-01-22", "unknown", "SUCCESS"),    # ukendt bruger
    ]

    r = post_termination_logins_of(former_employees, auth_log)
    assert len(r) == 2
    assert r[0] == ("server1", "2022-03-05", "aandersen", "SUCCESS")
    assert r[1] == ("server2", "2023-01-20", "bhansen", "SUCCESS")

def test_employee_index_of():
    employees = [
        ("Alice Andersen", "010190-1234", "aandersen", "Production"),
        ("Bob Hansen", "020278-5678", "bhansen", "Sales"),
        ("Clara Jensen", "150392-9876", "cjensen", "IT"),
    ]

    d = employee_index_of(employees)

    assert d["aandersen"] == 0
    assert d["bhansen"] == 1
    assert d["cjensen"] == 2
    assert len(d) == 3
    assert list(d.keys()) == ["aandersen", "bhansen", "cjensen"]

def test_employee_index_of():
    employees = [
        ("Alice Andersen", "010190-1234", "aandersen", "Production"),
        ("Bob Hansen", "020278-5678", "bhansen", "Sales"),
        ("Clara Jensen", "150392-9876", "cjensen", "IT"),
    ]

    d = employee_index_of(employees)

    assert d["aandersen"] == 0
    assert d["bhansen"] == 1
    assert d["cjensen"] == 2
    assert len(d) == 3
    assert list(d.keys()) == ["aandersen", "bhansen", "cjensen"]

def test_hostname_index_of():
    hosts = [
        ("server01", "00:1A:2B:3C:4D:5E", "Production"),
        ("server02", "00:1A:2B:3C:4D:5F", "Sales"),
        ("server03", "00:1A:2B:3C:4D:60", "IT"),
    ]

    d = hostname_index_of(hosts)

    assert d["server01"] == 0
    assert d["server02"] == 1
    assert d["server03"] == 2
    assert len(d) == 3
    assert list(d.keys()) == ["server01", "server02", "server03"]

def test_risk_score_of():
    employees = [
        ("Alice", "111", "alice", "Production"),
        ("Bob", "222", "bob", "Sales"),
    ]
    hosts = [
        ("server01", "00:1A:2B:3C:4D:5E", "Production"),
        ("server02", "00:1A:2B:3C:4D:5F", "Sales"),
    ]

    employees_index = username_index_of(employees)
    hosts_index = hostname_index_of(hosts)

    auth_log = [
        ("server01", "2025-01-01", "alice", "success"),  # green
        ("server02", "2025-01-02", "bob", "failure"),    # green (samme afd)
        ("server01", "2025-01-03", "bob", "failure"),    # yellow (anden afd, fejl)
        ("server02", "2025-01-04", "alice", "success"),  # red (anden afd, succes)
        ("server03", "2025-01-05", "unknown", "failure"),# red (ukendt bruger)
        ("server03", "2025-01-06", "unknown", "success") # critical (ukendt bruger)
    ]

    expected = ["green", "green", "yellow", "red", "red", "critical"]

    assert risk_score_of(auth_log, employees_index, hosts_index, employees, hosts) == expected

def test_risk_summary_of():
    auth_log = [
        ("pc-001", "2024-03-10T12:00:00", "jdoe", "success"),
        ("pc-002", "2024-03-11T09:30:00", "mdoe", "failure"),
        ("pc-003", "2024-03-12T08:15:00", "adoe", "success"),
        ("pc-004", "2024-03-13T14:45:00", "bdoe", "failure"),
    ]
    risk_scores = ["green", "red", "critical", "yellow"]

    summary = risk_summary_of(auth_log, risk_scores)
    assert summary == (1, 1, "2024-03-11T09:30:00", "2024-03-12T08:15:00")

def test_failed_login_count_by_username():
    auth_log = [
        ("pc-001", "2024-03-10T12:00:00", "alice", "success"),
        ("pc-002", "2024-03-10T12:05:00", "alice", "failure"),
        ("pc-003", "2024-03-10T12:10:00", "bob", "failure"),
        ("pc-004", "2024-03-10T12:15:00", "alice", "failure"),
        ("pc-005", "2024-03-10T12:20:00", "bob", "success"),
    ]
    expected = {
        "alice": 2,
        "bob": 1
    }
    assert failed_login_count_by_username(auth_log) == expected

def test_login_dates_by_username():
    auth_log = [
        ("pc-001", "2024-03-10T12:00:00", "alice", "success"),
        ("pc-002", "2024-03-11T08:15:00", "alice", "failure"),
        ("pc-003", "2024-03-09T09:30:00", "bob", "success"),
        ("pc-004", "2024-03-10T10:45:00", "bob", "failure"),
    ]

    expected = {
        "alice": ["2024-03-10", "2024-03-11"],
        "bob": ["2024-03-09", "2024-03-10"]
    }

    assert login_dates_by_username(auth_log) == expected

def test_failed_logins_by_username():
    auth_log = [
        ('srv01', '2024-03-10T12:00:00', 'alice', 'success'),
        ('srv02', '2024-03-10T12:30:00', 'alice', 'failure'),
        ('srv03', '2024-03-10T13:00:00', 'bob', 'failure'),
        ('srv01', '2024-03-10T14:00:00', 'charlie', 'success'),
    ]
    d = failed_logins_by_username(auth_log)
    assert len(d) == 2
    assert len(d['alice']) == 1
    assert len(d['bob']) == 1
    assert d['alice'][0][3] == 'failure'

def test_active_period_by_username():
    auth_log = [
        ('server1', '2024-02-01 08:15:00', 'alice', 'success'),
        ('server2', '2024-02-03 11:10:00', 'bob', 'failure'),
        ('server1', '2024-02-04 07:05:00', 'alice', 'failure'),
        ('server3', '2024-02-02 10:00:00', 'bob', 'success'),
        ('server1', '2024-02-05 08:32:00', 'alice', 'success')
    ]
    result = active_period_by_username(auth_log)
    assert result['alice'] == ('2024-02-01 08:15:00','2024-02-05 08:32:00')
    assert result['bob'] == ('2024-02-02 10:00:00', '2024-02-03 11:10:00')

def test_stats_by_hostname():
    auth_log = [
        ('server1', '2024-02-01 08:15:00', 'alice', 'success'),
        ('server1', '2024-02-04 07:05:00', 'bob', 'failure'),
        ('server2', '2024-02-03 11:10:00', 'bob', 'success'),
        ('server1', '2024-02-02 09:00:00', 'alice', 'failure'),
    ]
    result = stats_by_hostname(auth_log)
    assert ('server1', '2024-02-01 08:15:00', '2024-02-04 07:05:00', 3) in result
    assert ('server2', '2024-02-03 11:10:00', '2024-02-03 11:10:00', 1) in result
    assert len(result) == 2

def test_stats_by_hostname_and_username():
    auth_log = [
        ('server1', '2024-02-01 08:15:00', 'alice', 'success'),
        ('server1', '2024-02-02 09:00:00', 'alice', 'failure'),
        ('server1', '2024-02-03 10:00:00', 'bob', 'success'),
        ('server2', '2024-02-04 11:10:00', 'alice', 'failure'),
        ('server2', '2024-02-05 12:20:00', 'alice', 'success'),
    ]

    result = stats_by_hostname_and_username(auth_log)

    expected = [
        ('server1', 'alice', '2024-02-01 08:15:00', '2024-02-02 09:00:00', 2),
        ('server1', 'bob', '2024-02-03 10:00:00', '2024-02-03 10:00:00', 1),
        ('server2', 'alice', '2024-02-04 11:10:00', '2024-02-05 12:20:00', 2)
    ]

    # sammenlign som sæt (rækkefølgen i result er ikke vigtig)
    assert set(result) == set(expected)

##### ----- o4 opgaver her fra ----- #####

def test_count_by_currency_SS():
    transfers = [
        ('2025-01-04T12:00:00', 'ETH', 3, 'a03f', 'b077'),
        ('2025-01-04T12:05:00', 'USDT', 2, 'b077', 'a03f'),
        ('2025-01-04T12:10:00', 'ETH', 5, 'c0da', 'd084'),
        ('2025-01-04T12:15:00', 'BNB', 1, 'a03f', 'c0da'),
        ('2025-01-04T12:20:00', 'ETH', 4, 'e0fe', 'f052'),
    ]

    result = count_by_currency(transfers)
    expected = {'ETH': 3, 'USDT': 1, 'BNB': 1}
    assert result == expected

def test_count_by_currency_random():
    transfers = random_transfers(1000)
    result = count_by_currency(transfers)

    # Skal være en ordbog
    assert isinstance(result, dict)

    # Alle valutaer i result skal være kendte
    for currency in result:
        assert currency in CURRENCIES

    # Antallet af transaktioner skal stemme
    total_count = sum(result.values())
    assert total_count == 1000

    # Alle værdier skal være positive heltal
    for count in result.values():
        assert isinstance(count, int)
        assert count > 0

def test_count_by_date_manual_ss():
    transfers = [
        ("2025-01-01T10:00:00", "ETH", 5, "a03f", "b077"),
        ("2025-01-01T11:00:00", "BTC", 2, "b077", "c0da"),
        ("2025-01-02T09:00:00", "USDT", 3, "c0da", "a03f"),
        ("2025-01-02T09:30:00", "ETH", 1, "a03f", "f052"),
        ("2025-01-03T08:00:00", "BNB", 4, "e0fe", "b077"),
    ]
    result = count_by_date(transfers)
    assert result == {
        "2025-01-01": 2,
        "2025-01-02": 2,
        "2025-01-03": 1
    }

def test_count_by_date_random():
    transfers = random_transfers(1000, start='2025-01-01', end='2025-01-10')
    result = count_by_date(transfers)

    # skal være en ordbog
    assert isinstance(result, dict)

    # hver nøgle skal være en gyldig dato (ISO-format)
    for date in result.keys():
        assert len(date) == 10
        assert date[:4].isdigit()  # år
        assert date[4] == "-"
        assert date[5:7].isdigit()  # måned
        assert date[7] == "-"
        assert date[8:10].isdigit()  # dag

    # totalen skal være 1000 overførsler
    assert sum(result.values()) == 1000

def test_sum_by_date_and_currency_SS(): #simple set
    transfers = [
        ("2025-01-01T10:00:00", "ETH", 5, "a03f", "b077"),
        ("2025-01-01T11:00:00", "ETH", 2, "b077", "c0da"),
        ("2025-01-01T12:00:00", "USDT", 3, "c0da", "a03f"),
        ("2025-01-02T09:00:00", "ETH", 4, "a03f", "f052"),
        ("2025-01-02T10:00:00", "BNB", 7, "e0fe", "b077"),
        ("2025-01-02T11:00:00", "BNB", 3, "f052", "b077"),
    ]
    result = sum_by_date_and_currency(transfers)
    assert result == {
        ("2025-01-01", "ETH"): 7,
        ("2025-01-01", "USDT"): 3,
        ("2025-01-02", "ETH"): 4,
        ("2025-01-02", "BNB"): 10,
    }

def test_sum_by_date_and_currency_random():
    transfers = random_transfers(1000, start='2025-01-01', end='2025-01-05')
    result = sum_by_date_and_currency(transfers)

    # Skal være en ordbog
    assert isinstance(result, dict)

    # Alle nøgler skal være (dato, valuta)
    for key in result.keys():
        date, currency = key
        assert len(date) == 10
        assert currency in CURRENCIES

    # Summen af alle amounts skal være lig totalen af input
    total_input = sum(t[2] for t in transfers)
    total_result = sum(result.values())
    assert total_input == total_result

def test_active_timespan_by_address_manual():
    transfers = [
        ("2025-01-01T10:00:00", "ETH", 5, "a03f", "b077"),
        ("2025-01-01T12:00:00", "USDT", 3, "b077", "c0da"),
        ("2025-01-03T09:00:00", "BNB", 2, "a03f", "c0da"),
        ("2025-01-04T14:00:00", "ETH", 1, "d084", "a03f"),
    ]
    result = active_timespan_by_address(transfers)

    assert result["a03f"] == ("2025-01-01T10:00:00", "2025-01-04T14:00:00")
    assert result["b077"] == ("2025-01-01T10:00:00", "2025-01-01T12:00:00")
    assert result["c0da"] == ("2025-01-01T12:00:00", "2025-01-03T09:00:00")
    assert result["d084"] == ("2025-01-04T14:00:00", "2025-01-04T14:00:00")
    assert len(result) == 4

def test_active_timespan_by_address_random():
    transfers = random_transfers(1000, start='2025-01-01', end='2025-01-10')
    result = active_timespan_by_address(transfers)

    # Skal være en ordbog
    assert isinstance(result, dict)

    # Alle nøgler skal være kendte adresser
    for addr in result.keys():
        assert addr in ADDRESSES

    # Hver værdi skal være et (first, last)-par i korrekt rækkefølge
    for first, last in result.values():
        assert first <= last

    # Alle adresser i input bør findes i resultatet
    all_addrs = {t[3] for t in transfers} | {t[4] for t in transfers}
    assert all_addrs == set(result.keys())

def test_net_inflow_by_address_and_currency_manual():
    transfers = [
        ("2025-01-01T10:00:00", "ETH", 5, "a03f", "b077"),
        ("2025-01-02T11:00:00", "ETH", 2, "b077", "a03f"),
        ("2025-01-03T09:00:00", "USDT", 3, "a03f", "c0da"),
        ("2025-01-04T14:00:00", "ETH", 1, "d084", "a03f"),
    ]
    result = net_inflow_by_address_and_currency(transfers)

    # ETH
    assert result[("a03f", "ETH")] == -5 + 2 + 1  # -2
    assert result[("b077", "ETH")] == +5 - 2      # +3
    assert result[("d084", "ETH")] == -1          # -1
    # USDT
    assert result[("a03f", "USDT")] == -3
    assert result[("c0da", "USDT")] == +3

def test_net_inflow_by_address_and_currency_random():
    transfers = random_transfers(1000, start='2025-01-01', end='2025-01-10')
    result = net_inflow_by_address_and_currency(transfers)

    # Skal være en ordbog
    assert isinstance(result, dict)

    # Hver nøgle skal være et (adresse, valuta)-par
    for k in result.keys():
        addr, currency = k
        assert addr in ADDRESSES
        assert currency in CURRENCIES

    # Summen af alle inflows skal være 0 (for hver valuta er der lige mange afsendelser som modtagelser)
    totals = {c: 0 for c in CURRENCIES}
    for (addr, cur), value in result.items():
        totals[cur] += value
    for cur, net in totals.items():
        assert abs(net) < 1e-9  # eller == 0, men flydende afrunding

