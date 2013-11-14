class AddCpIdToActivationKeys < ActiveRecord::Migration
  def change
    add_column :activation_keys, :cp_id, :string
    add_index :activation_keys, :cp_id
  end
end
