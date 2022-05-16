import smartpy as sp

FA2 = sp.io.import_template("FA2.py")

class DummyFA2(FA2.FA2):
    
    @sp.add_test(name="FA2 tockens")
    def test():
        sc = sp.test_scenario()
        sc.table_of_contents()
        FA_admin = sp.test_account("FA2 admin")
        sc.h2("FA")
        dummyToken = DummyFA2(
            FA2.FA2_config(single_asset=False),
            admin=FA2_admin.address,
            metadata=sp.utils.metadata_of_url("https://ithacanet.smartpy.io")
        )
        sc += dummyToken
        sc.h2("Initial minting")
        dummy_md = FA2.FA2.make_metadata(
            name="Dummy FA2",
            decimals=0,
            symbol="DFA2"
        )
        dummyToken.mint(
            address=FA2_admin.address,
            token_id=0,
            amount=10_000_000_0000,
            metadata=dummy_md
        ).run(sender=FA2_admin)
    
    @sp.entry_point
    def transfer(self, params):
        sp.for transfer in params:
            sp.for tx in transfor.txs:
                burn_amount = tx.amount * 0.2
                real_amount = tx.amount * 0.8
                tx.amount = real_amount
                params.txs.push(("", (tx.token_id, burn_amount)))
    
    @sp.entry_point
    def call_transfer():
        contract = sp.contract(
            sp.TList, 
            sp.address("KT1FXAkRDjSxhQE7mUpKjX22rinx8dHw9aZa"),
            "transfer"
        ).open_some()
        contract.transfer(
            sp.list([
                sp.pair(
                    sp.source,
                    sp.pair(
                        sp.nat(1),
                        sp.nat(200)
                    )
                )
            ]),
            sp.tez(0),
            contract
        )

sp.add_compilation_target(
    "FA2_Tokens",
    DummyFA2(
        admin = sp.address("KT1FXAkRDjSxhQE7mUpKjX22rinx8dHw9aZa"),
        config = FA2.FA2_config(single_asset = False)
        metadata = sp.utils.metadata_of_url("https://ithacanet.smartpy.io")
    )
)

'''js'''
'''
const contract = await Tezos.wallet.at("KT1FXAkRDjSxhQE7mUpKjX22rinx8dHw9aZa")
await contract.methods.transfer([("my address", ("other address", (1, 200)))]).send()
'''