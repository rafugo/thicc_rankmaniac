#! /bin/bash

cd data/

python pagerank_map.py < input.txt | sort -k1,1 | python pagerank_reduce.py |
python process_map.py | sort -k1,1 | python process_reduce.py |

python pagerank_map.py | sort -k1.1 | python pagerank_reduce.py |
python process_map.py | sort -k1.1 | python process_reduce.py |

python pagerank_map.py | sort -k1.1 | python pagerank_reduce.py |
python process_map.py | sort | python process_reduce.py |

python pagerank_map.py | sort -k1.1 | python pagerank_reduce.py |
python process_map.py | sort -k1.1 | python process_reduce.py |

python pagerank_map.py | sort -k1.1 | python pagerank_reduce.py |
python process_map.py | sort -k1.1 | python process_reduce.py |

python pagerank_map.py | sort -k1.1 | python pagerank_reduce.py |
python process_map.py | sort -k1.1 | python process_reduce.py |

python pagerank_map.py | sort -k1.1 | python pagerank_reduce.py |
python process_map.py | sort -k1.1 | python process_reduce.py |

python pagerank_map.py | sort -k1.1 | python pagerank_reduce.py |
python process_map.py | sort -k1.1 | python process_reduce.py > output.txt
