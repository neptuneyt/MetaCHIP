import os


pwd_config_file = os.path.realpath(__file__)
config_file_path = '/'.join(pwd_config_file.split('/')[:-1])

config_dict = {'prodigal'     :  'prodigal',
               'hmmsearch'    :  'hmmsearch',
               'hmmfetch'     :  'hmmfetch',
               'hmmalign'     :  'hmmalign',
               'hmmstat'      :  'hmmstat',
               'mafft'        :  'mafft',
               'fasttree'     :  'FastTree',
               'blastp'       :  'blastp',
               'blastn'       :  'blastn',
               'makeblastdb'  :  'makeblastdb',
               'ranger_mac'   :  'Ranger-DTL-Dated.mac',
               'ranger_linux' :  'Ranger-DTL-Dated.linux',
               'path_to_hmm'  :  '%s/MetaCHIP_phylo.hmm'    % config_file_path,
               'circos_HGT_R' :  '%s/MetaCHIP_circos_HGT.R' % config_file_path}
