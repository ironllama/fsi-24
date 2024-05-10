def something(**allkws):
    print("ALL:", allkws)
    print("ALL KEYS:", allkws.keys())
    print("ALL VALS:", allkws.values())
    print("ALL ITEMS:", allkws.items())

    for key in allkws:
        print("K:", key, "V:", allkws[key])

    for key in allkws.keys():
        print("K:", key, "V:", allkws[key])

    for key_val_pair in allkws.items():
        print("K:", key_val_pair[0], "V:", key_val_pair[1])

    for (key, val) in allkws.items():
        print("K:", key, "V:", val)

    for fred, barney in allkws.items():
        print("K:", fred, "V:", barney)

something(name="cassowary", size="L", type="bird")
