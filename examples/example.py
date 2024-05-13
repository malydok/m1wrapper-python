# Full documentation available at: https://hub.YOUR_INSTANCE.molecule.one/docs/retro

from m1wrapper import MoleculeOneWrapper, Priority, DetailLevel, InvalidTargetStrategy

if __name__ == '__main__':
    # Get your token at https://retro.YOUR_INSTANCE.molecule.one/dashboard/settings/api-tokens
    token = 'YOUR_TOKEN'

    m1wrapper = MoleculeOneWrapper(token, 'https://retro.YOUR_INSTANCE.molecule.one')

    searches = m1wrapper.list_batch_searches()
    print('previous searches:', searches)

    search = m1wrapper.run_batch_search(
        targets=[
            'cc', 'O=C(Nc1cc(Nc2nc(-c3cnccc3)ccn2)c(cc1)C)c3ccc(cc3)CN3CCN(CC3)C'],
        parameters={'model': 'metro'},
        detail_level=DetailLevel.SYNTHESIS,
        priority=Priority.LOW,
        invalid_target_strategy=InvalidTargetStrategy.REJECT,
        name='API EXAMPLE'
    )
    print('created search:', search.search_id)

    search = m1wrapper.get_batch_search(search.search_id)
    print('got search:', search.search_id)

    status = search.get_status()
    print('status:', status)

    is_finished = search.is_finished()
    print('is finished:', is_finished)

    partial_results = search.get_partial_results()
    print("partial results:", partial_results)

    results = search.get_results(
        precision=4, only=['target_smiles', 'price', 'result'])
    print('results:', results)

    m1wrapper.delete_batch_search(search.search_id)
